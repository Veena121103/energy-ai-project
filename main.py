import joblib

# Load model
model = joblib.load("model.pkl")
print("✅ Model loaded successfully!")

# Sample input (same order as training)
sample = [[240.0, 10.0, 1.0, 0.0, 17.0, 0.2, 14, 21, 3]]

# Prediction
prediction = model.predict(sample)

print("⚡ Predicted Energy Consumption:", prediction)