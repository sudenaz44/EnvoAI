import geopandas as gpd
from pyproj import Geod

geod = Geod(ellps="WGS84")

def get_fault_line_distance(point, fault_shapefile="data/faultLine/gem_active_faults.shp"):
    """
    Calculates the shortest distance (in meters) from a given lat/lon point to the nearest fault line.
    
    Parameters:
        lat (float): Latitude of the point.
        lon (float): Longitude of the point.
        fault_shapefile (str): Path to the fault line shapefile.
    
    Returns:
        float: Minimum distance in meters.
    """
    # Create shapely point

    # Read fault lines from shapefile
    fault_lines = gpd.read_file(fault_shapefile)

    # Initialize minimum distance
    min_distance = float('inf')

    for _, row in fault_lines.iterrows():
        geom = row.geometry

        # Skip non-line geometries and empty ones
        if geom.is_empty or not geom.geom_type.startswith("Line"):
            continue

        # Project the point onto the line
        projected_point = geom.interpolate(geom.project(point))
        
        # Compute geodesic (WGS84) distance
        _, _, distance = geod.inv(point.x, point.y, projected_point.x, projected_point.y)

        # Update minimum distance
        if distance < min_distance:
            min_distance = distance

    return min_distance
