from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_response(text: str):
    console.print(Markdown(text))