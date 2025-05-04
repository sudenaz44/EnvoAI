import osmnx as ox

def get_infrastructure_availability(point, radius=1000):
    """
    Counts utility-related infrastructure (water, power, sewer) within the radius.
    """
    lon, lat = point
    tags = {
        'man_made': ['water_tower', 'wastewater_plant'],
        'power': True,
        'waterway': True
    }

    try:
        infra = ox.features_from_point((lat, lon), tags=tags, dist=radius)
        return len(infra)
    except:
        return 0
