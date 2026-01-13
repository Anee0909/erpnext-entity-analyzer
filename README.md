# ERPNext SalesInvoice Entity Analyzer

## Project Chosen
ERPNext – SalesInvoice Entity

## Objective
To understand how a real-world ERP system defines entities, relationships,
and business logic inside a large legacy codebase.

## What I Built
A Python-based analysis tool that:
- Extracts entity schema from ERPNext DocType JSON
- Identifies relationships between entities
- Extracts core business methods using Python AST
- Outputs structured JSON for further analysis

## What Works
- Field and relationship extraction from DocType JSON
- Business method discovery using AST parsing
- Robust file path handling using absolute paths

## Limitations
- Does not analyze runtime behavior
- No cross-module dependency graph
- Focused on a single entity (SalesInvoice)

## Learnings
- ERP systems encode critical business rules in code
- Separation of schema and logic improves maintainability
- Handling large codebases requires careful path management

## Next Steps
- Extract field-level validations
- Build dependency graphs between entities
- Add semantic search on extracted data

