import joblib

def load_model(model_path):
    return joblib.load(model_path)

if __name__ == "__main__":
    model = load_model("models/fraud_model.pkl")
    print(f"Modelo carregado com sucesso.")
