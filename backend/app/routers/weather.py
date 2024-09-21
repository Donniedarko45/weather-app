# app/routers/weather.py
import requests
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

API_KEY = "deaf674572572efb79ba5c22f7ed67c5"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@router.get("/{city}")
def get_weather(city: str):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=data.get("message"))

        # Return relevant weather data
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        return weather_data

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch weather data")
