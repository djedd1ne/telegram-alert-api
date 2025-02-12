import re

def is_valid_input(data):
    if not isinstance(data, dict):
        return False
    if not re.match(r"^[A-Za-z0-9\s_-]+$", data.get("Type", "")):
        return False
    if not re.match(r"^[A-Za-z0-9\s_-]+$", data.get("Name", "")):
        return False
    if len(data.get("Description", "")) > 4096:
        return False
    return True