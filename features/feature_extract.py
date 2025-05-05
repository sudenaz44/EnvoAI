
from shapely.geometry import Point
import pandas as pd

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


def extract_all_features(point, radius):
    return pd.DataFrame([{
        "fault_line_distance": get_fault_line_distance(point),
        "green_area_coverage": get_green_area_coverage(point, radius),
        "elevation": get_elevation(point),
        "slope_degree": get_slope_degree(point),
        "poi_density": get_poi_density(point, radius),
        "air_quality_index": get_air_quality_index(point),
        "transport_accessibility": get_transport_accessibility(point, radius),
        "infrastructure_availability": get_infrastructure_availability(point, radius),
        "protected_area_proximity": get_protected_area_proximity(point),
        "zoning_compliance": get_zoning_compliance(point, radius),
        "biodiversity_index": get_biodiversity_index(point),
        "disaster_risk_index": get_disaster_risk_index(point),
        # "land_use": get_land_use(point, radius),
        "noise_pollution_potential": get_noise_pollution_potential(point, radius),
        "socioeconomic_score": get_socioeconomic_score(point),
        "soil_type": get_soil_type(point),
        "water_proximity": get_water_proximity(point, radius)
        # other feature..
    }])
