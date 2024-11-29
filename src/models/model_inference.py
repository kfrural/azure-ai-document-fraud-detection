import joblib
import numpy as np

def run_inference(features):
    model = joblib.load("models/fraud_model.pkl")
    prediction = model.predict([features])
    return "Fraud Detected" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    features = np.random.rand(3)  
    result = run_inference(features)
    print(result)
