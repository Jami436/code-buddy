from rich.console import Console
from rich.table import Table

from utils.cli import show_help
from utils.banner import show_banner

from tools.file_manager import list_sandbox_files

console = Console()


class CommandHandler:
    """
    Handles all built-in CLI commands.
    Returns True if a command was handled.
    """

    def __init__(self):
        self.commands = {
            "/help": self.help_command,
            "/files": self.files_command,
            "/clear": self.clear_command,
            "/exit": self.exit_command,
            "/quit": self.exit_command,
            "exit": self.exit_command,
            "quit": self.exit_command,
        }

    def handle(self, command: str) -> bool:
        command = command.strip().lower()

        if command in self.commands:
            self.commands[command]()
            return True

        return False

    def help_command(self):
        show_help()

    def clear_command(self):
        console.clear()
        show_banner()
        show_help()

    def exit_command(self):
        console.print("\n Goodbye!")
        raise SystemExit

    def files_command(self):
        files = list_sandbox_files()

        if not files:
            console.print("[yellow]No Python files found in the sandbox.[/yellow]")
            return

        table = Table(title="Sandbox Files")
        table.add_column("File Name", style="cyan")

        for file in files:
            table.add_row(file)

        console.print(table)