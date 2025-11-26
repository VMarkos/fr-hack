# api/application/routes.py

from application import db
from application import models
from flask import Blueprint, jsonify, request
from . import copernicus_bridge as cb
from . import config
import numpy as np
import pandas as pd

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
    depth = 1.018 # HACK Hardcodeded for this endpoint
    point = cb.NCPoint(lat, lon, depth, time)
    bridge = cb.CopernicusBridge(config.Config.NCDATAPATH)
    if point not in bridge:
        return { "message": "Point not in range." }, 404
    sst = bridge.get_sst_at(point)
    if sst == np.nan:
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
