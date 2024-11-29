import pytest
import joblib
import os

def test_model_loading():
    model_path = "models/fraud_model.pkl"
    if not os.path.exists(model_path):
        pytest.fail(f"Modelo não encontrado: {model_path}")
    model = joblib.load(model_path)
    assert model is not None, "Falha ao carregar o modelo"
