# ERPNext SalesInvoice Code Analyzer

## Overview
This project is a lightweight **code analysis tool** built as part of an AI Engineering pre-internship assignment.  
It analyzes a real-world **ERPNext legacy codebase** to extract structured knowledge about a core business entity: **SalesInvoice**.

The goal is to demonstrate how enterprise systems encode business logic in code and how that knowledge can be programmatically extracted.

---

## Problem Statement
Legacy enterprise systems are large, complex, and poorly documented.  
Understanding entities, relationships, and business rules is time-consuming and error-prone.

This project addresses that problem by:
- Parsing entity schema definitions
- Extracting business logic methods
- Producing structured, machine-readable output

---

## Project Scope
- **Target System:** ERPNext (Open-source ERP)
- **Analyzed Entity:** SalesInvoice
- **Language:** Python
- **Approach:** Static code and metadata analysis

---

## Project Structure
```text
erpnext-entity-analyzer/
├── src/
│   ├── main.py              # Entry point for entity extraction
│   ├── extract_schema.py    # Extracts DocType schema from ERPNext JSON
│   └── extract_logic.py     # Extracts business logic methods
│
├── rag/
│   ├── build_index.py       # Builds embeddings for RAG
│   ├── query.py             # Semantic query interface
│   ├── texts.json           # Text chunks for RAG
│   └── embeddings.npy       # Vector embeddings
│
├── output.json              # Extracted SalesInvoice entity data
├── tests.md                 # Test scenarios and test cases
├── notes.md                 # Implementation notes
├── README.md                # Project documentation
└── .gitignore               # Ignored files
```

⚠️ Make sure:
- Triple backticks ``` are included
- `text` is written after the first backticks

---

### 🔹 Step 4: Save & Exit nano

- Press **Ctrl + O** → Enter  
- Press **Ctrl + X**

---

### 🔹 Step 5: Commit & push

```bash
git add README.md
git commit -m "Add project structure section"
git push origin main

