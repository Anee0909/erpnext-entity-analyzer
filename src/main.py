import os
import json
from extract_schema import extract_schema
from extract_logic import extract_methods

# Absolute path to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ERPNext paths
SCHEMA_PATH = os.path.join(
    BASE_DIR,
    "..", "..", "erpnext", "erpnext", "accounts", "doctype",
    "sales_invoice", "sales_invoice.json"
)

LOGIC_PATH = os.path.join(
    BASE_DIR,
    "..", "..", "erpnext", "erpnext", "accounts", "doctype",
    "sales_invoice", "sales_invoice.py"
)

schema = extract_schema(SCHEMA_PATH)
methods = extract_methods(LOGIC_PATH)

final_output = {
    "entity": schema["entity"],
    "fields": schema["fields"],
    "methods": methods,
    "relationships": schema["relationships"]
}

OUTPUT_PATH = os.path.join(BASE_DIR, "..", "output.json")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2)

print("✅ SalesInvoice extraction complete")

