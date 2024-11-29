import pytest
from src.processing.validate_output import validate_analysis

def test_validate_analysis():
    valid_data = {"field": "value"}
    invalid_data = None
    with pytest.raises(ValueError):
        validate_analysis(invalid_data)
    validate_analysis(valid_data)
