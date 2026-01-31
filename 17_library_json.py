"""
Portfolio: JSON (load, dump)
Topic: json module - serialize/deserialize data
"""

import json

DATA_FILE = "json_demo_data.json"


def main():
    print("=== JSON Module Demo ===\n")

    # Python dict/list to JSON string
    data = {"name": "Alice", "scores": [10, 20, 30], "active": True}
    json_str = json.dumps(data, indent=2)
    print("--- json.dumps (to string) ---")
    print(json_str)

    # JSON string to Python object
    parsed = json.loads(json_str)
    print("\n--- json.loads (from string) ---")
    print("  parsed['name'] =", parsed["name"])

    # Save to file
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Saved to {DATA_FILE} (json.dump)")

    # Load from file
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print("  Loaded from file:", loaded)


if __name__ == "__main__":
    main()
