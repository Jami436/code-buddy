def build_refactor_prompt(filename: str, code: str) -> str:
    return f"""
Refactor the following Python code.

Requirements:

-Preserve functionality
-Improve readability
-Follow PEP8
-Add type hints
-Add docstrings
-Remove duplicated code
-Improve variable names

Return ONLY the refactored code.

filename:
{filename}

Code:
{code}
"""