# Test Scenarios and Test Cases
ERPNext SalesInvoice Entity Analyzer

---

## Test Scenario 1: Successful Entity Extraction
**Description:**  
Verify that the tool correctly extracts SalesInvoice entity details from ERPNext.

**Preconditions:**  
- ERPNext repository is cloned correctly  
- SalesInvoice DocType files exist  

**Steps:**  
1. Navigate to `src/` directory  
2. Run `python3 main.py`  

**Expected Result:**  
- Console prints "SalesInvoice extraction complete"  
- `output.json` is generated  
- JSON contains entity, fields, methods, relationships  

---

## Test Scenario 2: Schema Parsing from DocType JSON
**Description:**  
Ensure entity schema is parsed correctly from `sales_invoice.json`.

**Expected Result:**  
- `fields` list is non-empty  
- `relationships` include Customer and Items  

---

## Test Scenario 3: Business Logic Method Extraction
**Description:**  
Verify that business logic methods are extracted from `sales_invoice.py`.

**Expected Result:**  
- Methods such as `validate` and `on_submit` appear in output  

---

## Test Scenario 4: Missing JSON File
**Description:**  
Verify tool behavior when schema file is missing.

**Steps:**  
1. Temporarily rename `sales_invoice.json`  
2. Run `python3 main.py`  

**Expected Result:**  
- Tool raises a clear FileNotFoundError  

---

## Test Scenario 5: Output Format Validation
**Description:**  
Ensure generated output is valid JSON and structured correctly.

**Expected Result:**  
- Output contains keys: entity, fields, methods, relationships  

---

## Test Scenario 6: Path Robustness
**Description:**  
Verify that absolute path handling works correctly.

**Expected Result:**  
- Tool runs successfully without path-related errors  

---

## Notes
These tests were executed manually to validate functionality and error handling.

