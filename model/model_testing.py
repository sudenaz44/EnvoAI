import pandas as pd
from model import predict_suitability

sample_data = pd.DataFrame([{
    "fault_line_distance": 12.5,
    "slope_degree": 5.2,
    "elevation": 120.0,
    "soil_type": "clay",
    "green_area_coverage": 0.3,
    "water_proximity": 1.8,
    "disaster_risk_index": 0.15,
    "biodiversity_index": 8.2,
    "protected_area_proximity": 3.0,
    "air_quality_index": 42,
    "noise_pollution_potential": 0.25,
    "transport_accessibility": 0.7,
    "infrastructure_availability": "high",
    "zoning_compliance": "yes",
    "poi_density": 48,
    "socioeconomic_score": 72.5
}])

score = predict_suitability(sample_data.iloc[0].to_dict())
print(score)
