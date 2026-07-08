import os
import shutil

# listing files
def list_sandbox_files(directory: str = "sandbox") -> list[str]:
    """
    Return all Python files in the sandbox directory.
    """

    try:
        return [
            file
            for file in os.listdir(directory)
            if file.endswith(".py")
        ]

    except Exception:
        return []

# reading file content
def read_file_content(file_name: str, directory: str = 'sandbox') -> str:
    """Read and return the content of a specific Python file from the sandbox."""
    try:
        path = os.path.join(directory, file_name)
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

# writing file content
def write_file_content(
    file_name: str,
    content: str,
    directory: str = "sandbox",
) -> str:
    """
    Write content to a file in the sandbox.

    If the file already exists, create a .bak backup before
    overwriting it with the new content.
    """

    try:
        path = os.path.join(directory, file_name)

        if os.path.exists(path):
            shutil.copy2(path, path + ".bak")

        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Successfully updated {file_name}"

    except Exception as e:
        return f"Error writing file: {e}"