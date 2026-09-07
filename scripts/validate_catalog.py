#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "skills.json").read_text(encoding="utf-8"))

errors = []
if len(data) != 20:
    errors.append(f"Expected exactly 20 skills, found {len(data)}")

repos = [x.get("repo") for x in data]
if len(repos) != len(set(repos)):
    errors.append("Duplicate repository entries found")

required = ["id", "name", "repo", "author", "category", "zh", "en", "preview", "license", "redistribution"]
for i, item in enumerate(data, 1):
    for key in required:
        if not item.get(key):
            errors.append(f"Entry {i} missing {key}")
    if item.get("id") != i:
        errors.append(f"Entry order mismatch at position {i}: id={item.get('id')}")
    for key in ["preview"]:
        if not str(item.get(key, '')).startswith('https://'):
            errors.append(f"Entry {i} {key} must use https://")

if errors:
    print("Catalog validation FAILED")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print(f"Catalog validation OK: {len(data)} unique skills, all required fields present.")
