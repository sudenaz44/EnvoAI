import geopandas as gpd
import osmnx as ox

def get_noise_pollution_potential(point, radius=1000):
    
    lon, lat = point

    roads = ox.graph_from_point((lat, lon), dist=radius, network_type='all')
    
    tags = {"landuse": ["industrial", "commercial"]}
    industrial_zones = ox.features_from_point((lat, lon), tags=tags, dist=radius)
    
    noise_level = 0  
    
    if len(roads.edges()) > 0: 
        noise_level += 50  
    
    if not industrial_zones.empty:  
        noise_level += 50 
    
    return noise_level

