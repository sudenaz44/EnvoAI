"""
    Project Name:   EnvoAI
"""

from shapely.geometry import Point


# --------------------------------------------
# Features IMPORT
# --------------------------------------------

from features.fault_line_distance import get_fault_line_distance
from features.slope_degree import get_slope_degree
from features.elevation import get_elevation
from features.poi_density import get_poi_density
from features.air_quality_index import get_air_quality_index
from features.transport_accessibility import get_transport_accessibility
from features.green_area_coverage import get_green_area_coverage
from features.infrastructure_availability import get_infrastructure_availability
from features.protected_area_proximity import get_protected_area_proximity
from features.zoning_compliance import get_zoning_compliance
from features.soil_type import get_soil_type
from features.water_proximity import get_water_proximity
from features.land_use import get_land_use
from features.disaster_risk_index import get_disaster_risk_index
from features.biodiversity_index import get_biodiversity_index
from features.noise_pollution_potential import get_noise_pollution_potential
from features.socioeconomic_score import get_socioeconomic_score




# --------------------------------------------
# Example input
# --------------------------------------------

def get_project_input():
    return {
        "latitude": 41.0164,
        "longitude": 28.9550,
        "radius": 1000,
    }

# --------------------------------------------
# Create Location
# --------------------------------------------
def get_project_location_point(data):
    return [data["longitude"], data["latitude"]]

def get_project_radius(data):
    return data["radius"]


# --------------------------------------------
# All Features
# --------------------------------------------

def extract_all_features(project_data):
    loc_point = get_project_location_point(project_data)
    radius = get_project_radius(project_data)

    features = {
        "fault_line_distance": get_fault_line_distance(Point(loc_point)),
        "soil_type": get_soil_type(loc_point),
        # "land_use": get_land_use(loc_point, radius),
        "water_proximity": get_water_proximity(loc_point, radius),
        "green_area_coverage": get_green_area_coverage(loc_point, radius),
        "elevation": get_elevation(loc_point),
        "slope_degree": get_slope_degree(loc_point),
        "poi_density": get_poi_density(loc_point, radius),
        "air_quality_index": get_air_quality_index(loc_point),
        "transport_accessibility": get_transport_accessibility(loc_point, radius),
        "infrastructure_availability": get_infrastructure_availability(loc_point, radius),
        "protected_area_proximity": get_protected_area_proximity(Point(loc_point)),
        "zoning_compliance": get_zoning_compliance(loc_point, radius),
        "disaster_risk_index": get_disaster_risk_index(loc_point),
        "biodiversity_index": get_biodiversity_index(loc_point),
        "noise_pollution_potential": get_noise_pollution_potential(loc_point, radius),
        "socioeconomic_score": get_socioeconomic_score(loc_point),
        # other feature..
    }

    return features



# --------------------------------------------
# Run
# --------------------------------------------

def main():
    project_data = get_project_input()
    feature_values = extract_all_features(project_data)

    print("[+] Project Location: ({}, {})".format(project_data["latitude"], project_data["longitude"]))
    print("[+] Feature Value:")
    for feature, value in feature_values.items():
        print(f"    - {feature}: {value}")

if __name__ == "__main__":
    main()
