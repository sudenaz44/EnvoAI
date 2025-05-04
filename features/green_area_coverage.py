import osmnx as ox

def get_green_area_coverage(point, radius=1000):
    """
    Calculates green area percentage within a radius using projected CRS.
    """
    lon, lat = point
    green_tags = {
        'leisure': ['park', 'garden'],
        'landuse': ['grass', 'forest'],
        'natural': ['wood', 'grassland']
    }

    try:
        green_areas = ox.features_from_point((lat, lon), tags=green_tags, dist=radius)

        if green_areas.empty:
            return 0

        # Convert geometries to projected CRS (e.g., UTM) for area calculation
        green_areas_proj = green_areas.to_crs(epsg=3857)  # Web Mercator, meters
        green_area = green_areas_proj.geometry.area.sum()

        total_area = 3.14 * (radius ** 2)
        return green_area / total_area
    except:
        return 0
