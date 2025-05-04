import requests

def get_soil_type(point):
    """
    Queries the SoilGrids API to retrieve soil type information at the specified location.

    Parameters:
        point (list): [longitude, latitude]

    Returns:
        str: Dominant soil type or 'unknown' if not available
    """
    lon, lat = point
    url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={lon}&lat={lat}&property=clay&depth=0-5cm"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        clay_content = data['properties']['layers'][0]['depths'][0]['values'].get('mean')

        if clay_content is None:
            return "unknown"

        return classify_soil_by_clay(clay_content)
    except Exception as e:
        print(f"[!] Error fetching soil data: {e}")
        return "unknown"

def classify_soil_by_clay(clay_pct):
    """
    Classifies soil based on clay content (simplified scale).

    Parameters:
        clay_pct (float): Percentage of clay content

    Returns:
        str: Soil type classification
    """
    clay_pct = (clay_pct / 10.0)  # convert to percentage

    if clay_pct < 15:
        return "sandy"
    elif 15 <= clay_pct < 30:
        return "loamy"
    else:
        return "clayey"

