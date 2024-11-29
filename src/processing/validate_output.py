def validate_analysis(data):
    if not data or not isinstance(data, dict):
        raise ValueError("Análise inválida. Os dados retornados estão vazios ou corrompidos.")
    print(f"Saída de análise válida: {data}")

if __name__ == "__main__":
    sample_data = {"field": "value"}
    validate_analysis(sample_data)
