import json

def extract_schema(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entity = data.get("name", "SalesInvoice")
    fields = []
    relationships = {}

    for field in data.get("fields", []):
        fieldname = field.get("fieldname")
        fieldtype = field.get("fieldtype")

        fields.append(fieldname)

        if fieldtype == "Link":
            relationships[fieldname] = field.get("options")

    return {
        "entity": entity,
        "fields": fields,
        "relationships": relationships
    }

