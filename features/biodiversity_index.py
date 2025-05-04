import requests

def get_biodiversity_index(point):
    
    lon, lat = point
    
    # GBIF API URL
    url = f"https://api.gbif.org/v1/occurrence/search?lat={lat}&lon={lon}&radius=50&limit=5"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["results"]:
            species = [entry["speciesKey"] for entry in data["results"]]
            return len(species)
        else:
            return 0
    except Exception as e:
        return f"Error fetching biodiversity data: {e}"

