import requests

def get_air_quality_index(point):
    """
    Retrieves PM2.5 concentration for the location using Open-Meteo API.
    """
    lon, lat,  = point
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=pm2_5"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pm25 = data.get("hourly", {}).get("pm2_5", [])[0]
        return pm25 if pm25 is not None else 0
    return 0
