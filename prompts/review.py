def build_review_prompt(filename: str, code: str) -> str:
    return f"""
Perform a professional code review.

Review categories:

-Correctness
-Readability
-Architecture
-Performance
-Security
-Maintainability

Assign a severity:

HIGH
MEDIUM
LOW

Filename:
{filename}

Code:
{code}
"""