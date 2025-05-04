import osmnx as ox

def get_zoning_compliance(point, radius=1000, expected_zone='residential'):
    """
    Checks if the land use matches the expected zoning (simplified).
    """
    lon, lat = point
    tags = {'landuse': True}
    try:
        zoning_data = ox.features_from_point((lat, lon), tags=tags, dist=radius)
        if zoning_data.empty:
            return False
        zone_types = zoning_data['landuse'].unique()
        return expected_zone in zone_types
    except:
        return False
