import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "not-so-secret"

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "sqlite:///your_database.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
