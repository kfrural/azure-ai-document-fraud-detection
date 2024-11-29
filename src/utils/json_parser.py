import json

def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    sample_data = {"example": "data"}
    write_json("data/processed/sample.json", sample_data)
    print(read_json("data/processed/sample.json"))
