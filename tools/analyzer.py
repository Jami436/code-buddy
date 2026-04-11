import subprocess
import os

def run_flake8_analysis(file_name: str, directory: str = 'sandbox') -> str:
    """Run flake8 on a specific file and return any style or syntax errors found."""
    path = os.path.join(directory, file_name)
    try:
        result = subprocess.run(['flake8', path], capture_output=True, text=True)
        return result.stdout if result.stdout else "No style/syntax errors found."
    except FileNotFoundError:
        return "Error: flake8 is not installed or not found in PATH."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def run_mypy_analysis(file_name: str, directory: str = 'sandbox') -> str:
    """Run mypy type checking on a specific file and return any type errors found."""
    path = os.path.join(directory, file_name)
    try:
        result = subprocess.run(['mypy', path, '--ignore-missing-imports'], capture_output=True, text=True)
        return result.stdout if result.stdout else "No type errors found."
    except Exception as e:
        return f"Error running mypy: {str(e)}"