import pandas as pd
import joblib

def predict(feature_dict: dict, model_path="./data/envo_model.pkl") -> float:
    model = joblib.load(model_path)
    df = pd.DataFrame([feature_dict])
    return model.predict(df)[0]
