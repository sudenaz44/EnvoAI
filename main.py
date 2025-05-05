
from model.model_predict import predict
from features.feature_extract import extract_all_features
from mapping.location import *

def main():
    lat, lon, radius = get_project_input(lat=55.486, lon=28.564, radius=1000)
    feature_values = extract_all_features(point=[lon, lat], radius=radius)

    score = predict(feature_values.iloc[0].to_dict())

    print("[+] Project Location: ({}, {})".format(lat, lon))
    print("[+] Feature Score: ({})".format(score))

    print("[+] Feature Values:")
    for column in feature_values.columns:
        print(f"    [-] {column}: {feature_values.at[0, column]}")

if __name__ == "__main__":
    main()
