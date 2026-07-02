from rich.console import Console

console = Console()


def show_help():
    console.print(
        """
[bold cyan]Available Commands[/bold cyan]

[green]/help[/green]      Show help
[green]/clear[/green]     Clear terminal
[green]/exit[/green]      Exit Code Buddy
"""
    )