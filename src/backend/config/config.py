import os
from datetime import timedelta


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
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_IDENTITY_CLAIM = "user_id"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)

class ProductStatus:
    AVAILABLE = "available"
    OUT_OF_STOCK = "out of stock"
