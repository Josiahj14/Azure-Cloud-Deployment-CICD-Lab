import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
status_file = project_root / "src" / "status.json"

with status_file.open(encoding="utf-8") as file:
    data=json.load(file)

if not isinstance(data, dict) or not isinstance(data.get("services"), list):
    raise ValueError("Expected a services list")

services = data["services"]

if not services:
    raise ValueError("Services list cannot be empty")

valid_statuses = {"operational", "maintenance"}

for service in services:
    if not isinstance(service, dict):
        raise ValueError("Each service must be a object")

    name = service.get("name")
    status = service.get("status")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Service name is missing")

    if not isinstance(status, str) or status not in valid_statuses:
        raise ValueError(f"Invalid status for '{name}': {status}")

print(f"Validation passed: {len(services)} services")