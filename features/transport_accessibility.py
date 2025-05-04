import osmnx as ox

def get_transport_accessibility(point, radius=1000):
    """
    Calculates transportation accessibility based on road density.
    """
    lon, lat = point
    try:
        graph = ox.graph_from_point((lat, lon), dist=radius, network_type='drive')
        edge_length = sum([d['length'] for u, v, k, d in graph.edges(keys=True, data=True)])
        return edge_length / (radius * radius * 3.14)  # meters per m2
    except:
        return 0
