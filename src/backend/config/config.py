import os


class Config:
    # PostgreSQL configuration
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", None)
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", None)
    POSTGRES_USER = os.environ.get("POSTGRES_USER", None)
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", None)
    POSTGRES_DB = os.environ.get("POSTGRES_DB", None)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "thisisasecret"
