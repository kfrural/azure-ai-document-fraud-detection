import json

def validate_analysis(data):
    if not isinstance(data, dict) or len(data) == 0:
        raise ValueError("Análise inválida. Os dados retornados estão vazios ou corrompidos.")
    print(f"Saída de análise válida: {json.dumps(data, indent=2)}")

if __name__ == "__main__":
    sample_data = {"field": "value"}
    validate_analysis(sample_data)
