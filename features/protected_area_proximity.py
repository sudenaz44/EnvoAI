import geopandas as gpd
from shapely.geometry import Point

def get_protected_area_proximity(point, protected_shapefile="data/protectedArea/eco_p_c_2017.shp"):
    """
    Calculates the closest distance to any protected natural area using the distance method for polygons.
    """
    
    try: 
        protected_areas = gpd.read_file(protected_shapefile)
        
        point = Point(point)

        min_distance = float('inf')
        for _, row in protected_areas.iterrows():
            geom = row.geometry
            if geom.is_empty:
                continue
            
            # Calculate the distance between the point and the geometry (polygon)
            distance = point.distance(geom)

            # Update the minimum distance if necessary
            min_distance = min(min_distance, distance)
        
        return min_distance
    except:
        return 0
