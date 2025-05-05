import joblib

# Modeli dışa aktar
model_path = "./data/envo_model.pkl"
joblib.dump(pipeline, model_path)

# Örnek tahmin: ilk test verisindeki skor
sample_features = X_test.iloc[0:1]
sample_prediction = pipeline.predict(sample_features)[0]

model_path, sample_prediction
