import osmnx as ox

def get_poi_density(point, radius=1000):
    """
    Counts the number of POIs (like shops, schools, pharmacies) within a given radius.
    """
    lon, lat = point
    tags = {
        'amenity': True,     # e.g. school, hospital
        'shop': True,        # e.g. market, clothing
        'office': True,      # business offices
    }

    try:
        pois = ox.features_from_point((lat, lon), tags=tags, dist=radius)
        return len(pois)
    except:
        return 0
