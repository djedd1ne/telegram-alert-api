import pytest
from app.utils import is_valid_input

@pytest.mark.parametrize("data, expected", [ #Valid
    ({"Type": "Warning", "Name": "Backup Failure", "Description": "The backup failed"}, True),
    ({"Type": "Info", "Name": "System Update", "Description": "Routine update completed"}, True),
    ({"Type": "Alert", "Name": "Server Down", "Description": "Urgent: Restart required"}, True),
    #Invalid
    ("Not a dictionary", False),
    ({"Type": "Invalid@Type", "Name": "Valid Name", "Description": "Test"}, False),
    ({"Type": "Valid Type", "Name": "Invalid#Name", "Description": "Test"}, False),
    ({"Type": "Valid Type", "Name": "Valid Name", "Description": "X" * 5000}, False),
])
def test_is_valid_input(data, expected):
    assert is_valid_input(data) == expected