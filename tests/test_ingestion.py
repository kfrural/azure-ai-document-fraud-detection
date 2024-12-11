import pytest
from src.ingestion.validate_input import validate_document

def test_validate_document():
    with pytest.raises(FileNotFoundError):
        validate_document("invalid_path.pdf")
    with pytest.raises(ValueError):
        validate_document("invalid_file.txt")
    validate_document("data/samples/sample_doc.pdf")

