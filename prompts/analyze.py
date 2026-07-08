def build_analyze_prompt(filename: str, code: str) -> str:
    return f"""
Analyze the following Python file.

Filename:
{filename}

Review it for:

-Bugs
-Code smells
-Readability
-Performance
-Security
-Best practices
-Maintainability

Give your response in this format:

## Summary

## Issues Found

## Recommendations

Code:

{code}
"""