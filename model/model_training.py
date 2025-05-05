import pandas as pd

data = pd.DataFrame([
    {
        "fault_line_distance": 2000,
        "land_use": "residential",
        "soil_type": "sandy",
        "green_area_coverage": 12.5,
        # ...
        "suitability_score": 4  # Bu etiketi sen vereceksin (manuel, uzman, geçmiş veri vs.)
    },
    ...
])


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data["land_use"] = le.fit_transform(data["land_use"])



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

X = data.drop(columns=["suitability_score"])
y = data["suitability_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model R^2 score: {score}")


import joblib

model = joblib.load("model.pkl")
prediction = model.predict([[
    fault_line_distance, land_use_encoded, green_area_coverage, ...
]])
