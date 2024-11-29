import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def create_and_save_model():
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "models/fraud_model.pkl")
    print("Modelo salvo em: models/fraud_model.pkl")

if __name__ == "__main__":
    create_and_save_model()