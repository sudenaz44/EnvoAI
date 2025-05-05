import osmnx as ox
import geopandas as gpd

def get_land_use(point, radius=1000):
    
    lon, lat = point
    try:
        # (lat, lon) -> bounding box (north, south, east, west)
        north, south, east, west = ox.utils_geo.bbox_from_point((lat, lon), dist=radius)
        bbox = (west, south, east, north)

        tags = {
            "landuse": ["residential", "commercial", "industrial", "forest", "farmland", "grass"],
            "natural": ["wood", "scrub", "grassland"]
        }

        gdf = ox.features_from_bbox(bbox=bbox, tags=tags)

        if gdf.empty:
            return 0

        for key in ["landuse", "natural"]:
            if key in gdf.columns:
                vals = gdf[key].dropna().unique()
                if len(vals) > 0:
                    return vals[0]

        return 0

    except:
        return 0
