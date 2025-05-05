import osmnx as ox
from geopy.distance import geodesic

def get_water_proximity(point, radius=1000):
    """
    Calculates the distance (in meters) to the nearest water body (river, lake, or coastline)
    using OpenStreetMap data.

    Parameters:
        point (list): [longitude, latitude]
        radius (int): Search radius in meters

    Returns:
        float: Distance to the nearest water body in meters
    """
    lon, lat = point
    tags = {"natural": ["water"], "waterway": True}
    
    try:
        water_bodies = ox.features_from_point(center_point=(lat, lon), tags=tags, dist=radius)

        if water_bodies.empty:
            return 0  # No water body found within the radius

        min_distance = float("inf")

        for _, feature in water_bodies.iterrows():
            geometry = feature.geometry

            if geometry.is_empty:
                continue

            if geometry.geom_type == "Point":
                coords = (geometry.y, geometry.x)
            else:
                # Get nearest coordinate from complex geometries (like LineString or Polygon)
                coords = (geometry.centroid.y, geometry.centroid.x)

            distance = geodesic((lat, lon), coords).meters
            if distance < min_distance:
                min_distance = distance

        return min_distance
    except:
        return 0
