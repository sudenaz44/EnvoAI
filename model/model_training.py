from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import numpy as np

# Bu örnekte, çeşitli kolonlardan ağırlıklı ortalama ile bir skor üretiliyor.
np.random.seed(42)
df["suitability_score"] = (
    0.2 * df["green_area_coverage"] * 100 +
    0.2 * (1 - df["disaster_risk_index"]) * 100 +
    0.1 * df["biodiversity_index"] * 10 +
    0.1 * (1 - df["noise_pollution_potential"]) * 100 +
    0.1 * df["transport_accessibility"] * 100 +
    0.1 * df["infrastructure_availability"].astype(int) * 100 +
    0.1 * df["zoning_compliance"].astype(int) * 100 +
    0.1 * df["socioeconomic_score"]
)

# Özellik ve hedef değişken ayrımı
X = df.drop(columns=["suitability_score"])
y = df["suitability_score"]

# Kategorik ve sayısal sütunları belirle
categorical_features = ["soil_type", "infrastructure_availability", "zoning_compliance"]
numerical_features = [col for col in X.columns if col not in categorical_features]

# Pipeline: Kategorik sütunlar için OneHotEncoder, diğerleri direkt
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
], remainder="passthrough")

# Model ve pipeline tanımı
model = RandomForestRegressor(n_estimators=100, random_state=42)
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", model)
])

# Eğitim/test verisi bölünmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model eğitimi
pipeline.fit(X_train, y_train)

# Test skorları
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# 5-fold cross-validation skoru
cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring="neg_root_mean_squared_error")

{
    "RMSE (test set)": rmse,
    "CV RMSE (mean)": -np.mean(cv_scores),
    "CV RMSE (std)": np.std(cv_scores)
}
