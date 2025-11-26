# api/application/models.py

import csv
from flask_sqlalchemy import SQLAlchemy
from application import db
from .utils import safe_cast

MED_FISH_TEMP = "../datasets/local/medfishtemp.csv"


class Fish(db.Model):
    species = db.Column(db.String(100), primary_key=True)
    taxon = db.Column(db.String(100))
    pref_temp = db.Column(db.Float)
    t_min = db.Column(db.Float)
    min_metric = db.Column(db.String(100))
    t_max = db.Column(db.Float)
    max_metric = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def clear_db() -> None:
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()


def populate_db() -> None:
    kw_map = {
        "ScientificName": "species",
        "Taxon": "taxon",
        "PrefTemp": "pref_temp",
        "tmin": "t_min",
        "minmetric": "min_metric",
        "tmax": "t_max",
        "maxmetric": "max_metric",
    }
    float_kws = ("PrefTemp", "tmin", "tmax")
    with open(MED_FISH_TEMP, "r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for r in csv_reader:
            kwargs = {
                kw_map[c]: (safe_cast(float, v) if c in float_kws else v.lower())
                for c, v in zip(header, r)
            }
            new_fish_entry = Fish(**kwargs)
            db.session.add(new_fish_entry)
            db.session.commit()


def init_db() -> None:
    # clear_db()
    db.create_all()
    populate_db()


if __name__ == "__main__":
    init_db()
