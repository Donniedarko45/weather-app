# app/config.py
import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/db_name")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    API_KEYS = {
        "satellite_data": os.getenv("SATELLITE_API_KEY"),
        "weather_data": os.getenv("WEATHER_API_KEY")
    }
