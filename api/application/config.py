# api/application/config.py

import numpy as np
from datetime import date

class Config:
    """API configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    NCDATAPATH = "../datasets/local/copmedgr.nc"
    TEST_TS = np.arange(date(2023,11,1), date(2025,11,30))
