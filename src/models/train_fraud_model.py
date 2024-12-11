from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
from sklearn.datasets import make_classification

def train_model():
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Modelo treinado com precisão: {accuracy * 100:.2f}%")
    
    joblib.dump(model, "models/fraud_model.pkl")

if __name__ == "__main__":
    train_model()
