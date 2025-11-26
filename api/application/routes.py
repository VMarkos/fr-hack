# api/application/routes.py

from application import db
from application import models
from flask import Blueprint, jsonify, request

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")


@api_bp.route("/fishPreferredTemperature", methods=["GET"])
def fish_preferred_temperature():
    """Get preferred temperature for fish species based on MedFaunaTp"""
    species = request.args.get("species")
    species = species.lower()
    fish = (
        db.session.execute(db.select(models.Fish).filter_by(species=species))
        .scalars()
        .all()
    )
    if not fish:
        return {"message": "Fish not found!"}, 404
    print(fish[0], type(fish[0]))
    resp = jsonify(fish[0].as_dict())
    return resp, 200
