import requests

def get_elevation(point):
    """
    Retrieves elevation (in meters) for a given location using Open-Elevation API.
    Input: point (longitude, latitude)
    Output: elevation in meters (float)
    """
    lon, lat = point
    
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    response = requests.get(url)

    try: 
        if response.status_code == 200:
            elevation = response.json()["results"][0]["elevation"]
            return elevation
        else:
            return 0
    except:
        return 0