import os

def list_sandbox_files(directory: str = 'sandbox') -> list:
    """List all Python files in the sandbox directory."""
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.py')]
        return files if files else "No Python files found in sandbox."
    except Exception as e:
        return f"Error accessing directory: {str(e)}"

def read_file_content(file_name: str, directory: str = 'sandbox') -> str:
    """Read and return the content of a specific Python file from the sandbox."""
    try:
        path = os.path.join(directory, file_name)
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file_content(file_name: str, content: str, directory: str = 'sandbox') -> str:
    """Write the given content to a specific file in the sandbox, overwriting existing content."""
    try:
        path = os.path.join(directory, file_name)
        with open(path, 'w') as f:
            f.write(content)
        return f"Successfully wrote changes to {file_name}."
    except Exception as e:
        return f"Error writing file: {str(e)}"