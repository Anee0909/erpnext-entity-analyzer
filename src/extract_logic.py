import ast

def extract_methods(py_path):
    with open(py_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    methods = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            methods.append(node.name)

    return methods

