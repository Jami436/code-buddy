from rich.console import Console

console = Console()


def show_help():
    console.print("\n[bold cyan]Available Commands[/bold cyan]\n")

    console.print("[green]/help[/green]             Show help")
    console.print("[green]/files[/green]            List Python files in the sandbox")
    console.print("[green]/read <file>[/green]      Display a Python file")
    console.print("[green]/refactor <file>      Refactor a Python file")
    console.print("[green]/clear[/green]            Clear terminal")
    console.print("[green]/exit[/green]             Exit Code Buddy")