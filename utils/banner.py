from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner():
    panel = Panel.fit(
        "[bold cyan] Code Buddy v2.0[/bold cyan]\n"
        "[green]Your AI Software Engineer[/green]",
        border_style="bright_blue",
    )

    console.print(panel)