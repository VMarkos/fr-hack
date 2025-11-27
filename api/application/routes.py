# api/application/routes.py

from application import db
from application import models
from flask import Blueprint, jsonify, request
from . import copernicus_bridge as cb
from . import config
import numpy as np
import pandas as pd
from datetime import timedelta, date
import math

from . import marineHeatWaves as mhw

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/fishPreferredTemperature", methods=["GET"])
def fish_preferred_temperature():
    """Get preferred temperature for fish species based on MedFaunaTp."""
    species = request.args.get("species")
    species = species.lower()
    fish = (
        db.session.execute(db.select(models.Fish).filter_by(species=species))
        .scalars()
        .all()
    )
    if not fish:
        return {"message": "Fish not found!"}, 404
    resp = jsonify(fish[0].as_dict())
    return resp, 200

@api_bp.route("/sstAt", methods=["GET"])
def sst_at():
    """Get SST at certain lat, lon, depth, and time."""
    lat = np.float32(request.args.get("lat"))
    lon = np.float32(request.args.get("lon"))
    time = pd.to_datetime(request.args.get("time"), format="%Y-%m-%d")
    depth = np.float32(request.args.get("depth")) or 1.018
    point = cb.NCPoint(lat, lon, depth, time)
    bridge = cb.CopernicusBridge(config.Config.NCDATAPATH)
    if point not in bridge:
        return { "message": "Point not in range." }, 404
    sst = bridge.get_sst_at(point)
    if np.isnan(sst):
        sst = None
    else:
        sst = float(sst)
    resp = {
        "lat": float(lat), 
        "lon": float(lon),
        "depth": depth,
        "time": str(time),
        "sst": sst,
    }
    return resp, 200

@api_bp.route("/upcomingMHW", methods=["GET"])
def upcoming_mhw():
    lat = np.float32(request.args.get("lat"))
    lon = np.float32(request.args.get("lon"))
    depth = np.float32(request.args.get("depth")) or 1.018
    time = pd.to_datetime(request.args.get("time"), format="%Y-%m-%d")
    bridge = cb.CopernicusBridge(config.Config.NCDATAPATH)
    species = request.args.get("species").lower()
    fish = (
        db.session.execute(db.select(models.Fish).filter_by(species=species))
        .scalars()
        .all()
    )
    fish_dict = fish[0].as_dict()

    CTA = ['No action', 'Less feeding', 'No feeding', 'No feeding, spread further']

    # Play with timestamps
    ts = np.fromiter((t for t in config.Config.TEST_TS if t <= time + timedelta(days=7)), dtype='datetime64[D]')
    ssts = np.fromiter((bridge.get_sst_at(cb.NCPoint(lat, lon, depth, t)) for t in ts), dtype=np.float32)
    ots = ts.astype(int) 
    mhws, clim = mhw.detect(ots, ssts)
    if mhws['n_events'] == 0:
        resp = {
            "upcoming_mhw": False,
            "max_intensity": None,
            "avg_intensity": None,
            "cum_intensity": None,
            "duration": None,
            "start_date": None,
            "predicted_sst": [],
            "severity": 0,
            "call_to_action": CTA[0],
        }
        return resp, 200
    latest_mhw = np.argmax(mhws['date_start'])
    upcoming_mhw = False
    lsdate = mhws['date_start'][latest_mhw]
    lsdate = lsdate.replace(year=lsdate.year + 1970)
    if pd.Timestamp(lsdate) >= time:
        upcoming_mhw = True
    max_temp = float(ssts[-7:].max())
    score = (max_temp - fish_dict['pref_temp']) / (fish_dict['t_max'] - fish_dict['pref_temp'])
    severity = min(math.ceil(score * 3), 3)
    # Returns the latest MHW in any case
    resp = {
        "upcoming_mhw": upcoming_mhw,
        "max_intensity": mhws['intensity_max'][latest_mhw],
        "avg_intensity": mhws['intensity_mean'][latest_mhw],
        "cum_intensity": mhws['intensity_cumulative'][latest_mhw],
        "duration": mhws['duration'][latest_mhw],
        "start_date": lsdate,
        "predicted_sst": [float(s) for s in ssts[-7:]],
        "severity": severity,
        "call_to_action": CTA[severity],
    }
    return resp, 200
