# api/application/config.py


class Config:
    """API configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    NCDATAPATH = "../datasets/local/copmedgr.nc"
