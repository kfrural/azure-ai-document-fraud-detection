def preprocess_data(data):
    suspicious_patterns = ["fake_id", "invalid", "expired"]
    alerts = [field for field, value in data.items() if any(p in str(value).lower() for p in suspicious_patterns)]
    return alerts

if __name__ == "__main__":
    sample_data = {"document_id": "12345", "status": "expired"}
    alerts = preprocess_data(sample_data)
    print(alerts)
