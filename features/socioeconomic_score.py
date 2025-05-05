import requests

def get_socioeconomic_score(point):
    
    lon, lat = point 
    
    country_code = get_country_code(lat, lon)
    
    # World Bank API URL
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.PCAP.CD?format=json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data[1]:
            gdp_per_capita = data[1][0]["value"]
            return gdp_per_capita
        else:
            return 0
    except:
        return 0


def get_country_code(lat, lon):
    # Nominatim API URL
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "address" in data and "country_code" in data["address"]:
            country_code = data["address"]["country_code"].upper()
            return country_code
        else:
            return 0
    except:
        return 0

