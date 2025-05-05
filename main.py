
from model.model_predict import predict
from features.feature_extract import extract_all_features
from mapping.location import *

def main():
    lat, lon, radius = get_project_input(lat=57, lon=14, radius=1000)
    feature_values = extract_all_features(point=[lon, lat], radius=radius)

    score = predict(feature_values.iloc[0].to_dict())

    print("[+] Project Location: ({}, {})".format(lat, lon))
    print("[+] Feature Score: ({})".format(score))

if __name__ == "__main__":
    main()
