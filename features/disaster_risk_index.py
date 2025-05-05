import requests
import math

def get_disaster_risk_index(point):
    lon, lat = point
    
    # USGS Earthquake API URL
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude={lat}&longitude={lon}&maxradius=100"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["features"]:
            recent_earthquake = data["features"][0]
            magnitude = recent_earthquake["properties"]["mag"]
            place = recent_earthquake["properties"]["place"]
            coordinates = recent_earthquake["geometry"]["coordinates"]
            distance = calculate_distance(lon, lat, coordinates[0], coordinates[1])
            
            magnitude_score = magnitude ** 2  
            distance_score = max(1, 1000 / distance)  
            
            risk_score = magnitude_score * distance_score
            return risk_score
        else:
            return 0
    except:
        return 0


def calculate_distance(lon1, lat1, lon2, lat2):
    R = 6371  # Earth radius (km)
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c 
    return distance * 1000




