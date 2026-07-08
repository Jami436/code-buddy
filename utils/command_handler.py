from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel

from utils.cli import show_help
from utils.banner import show_banner
from utils.command_result import CommandResult

from tools.file_manager import (
    list_sandbox_files,
    read_file_content,
)

from prompts.analyze import build_analyze_prompt
from prompts.refactor import build_refactor_prompt

console = Console()


class CommandHandler:
    """
    Handles CLI commands.

    Returns a CommandResult.
    """

    def __init__(self):
        self.commands = {
            "/help": self.help_command,
            "/files": self.files_command,
            "/read": self.read_command,
            "/analyze": self.analyze_command,
            "/refactor": self.refactor_command,
            "/clear": self.clear_command,
            "/exit": self.exit_command,
            "/quit": self.exit_command,
            "exit": self.exit_command,
            "quit": self.exit_command,
        }

    def handle(self, command: str) -> CommandResult:
        command = command.strip()

        parts = command.split(maxsplit=1)
        base_command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        if base_command in self.commands:
            return self.commands[base_command](argument)

        return CommandResult(False)

    def help_command(self, _=""):
        show_help()
        return CommandResult(True)

    def clear_command(self, _=""):
        console.clear()
        show_banner()
        show_help()
        return CommandResult(True)

    def exit_command(self, _=""):
        console.print("\n👋 Goodbye!")
        raise SystemExit

    def files_command(self, _=""):
        files = list_sandbox_files()

        if not files:
            console.print("[yellow]No Python files found in the sandbox.[/yellow]")
            return CommandResult(True)

        table = Table(title="Sandbox Files")
        table.add_column("File Name", style="cyan")

        for file in files:
            table.add_row(file)

        console.print(table)

        return CommandResult(True)

    def read_command(self, filename=""):
        if not filename:
            console.print("[yellow]Usage: /read <filename>[/yellow]")
            return CommandResult(True)

        content = read_file_content(filename)

        if content.startswith("Error"):
            console.print(f"[red]{content}[/red]")
            return CommandResult(True)

        syntax = Syntax(
            content,
            "python",
            line_numbers=True,
            word_wrap=True,
        )

        console.print(
            Panel(
                syntax,
                title=filename,
                border_style="cyan",
            )
        )

        return CommandResult(True)

    def analyze_command(self, filename=""):
        if not filename:
            console.print("[yellow]Usage: /analyze <filename>[/yellow]")
            return CommandResult(True)

        content = read_file_content(filename)

        if content.startswith("Error"):
            console.print(f"[red]{content}[/red]")
            return CommandResult(True)

        prompt = build_analyze_prompt(
            filename,
            content,
        )

        return CommandResult(
            handled=True,
            ai_prompt=prompt,
        )

    def refactor_command(self, filename=""):
        if not filename:
            console.print("[yellow]Usage: /refactor <filename>[/yellow]")
            return CommandResult(True)
        
        content = read_file_content(filename)

        if content.startswith("Error"):
            console.print(f"[red]{content}[/red]")
            return CommandResult(True)
        
        prompt = build_refactor_prompt(
            filename,
            content,
        )

        return CommandResult(
            handled = True,
            ai_prompt=prompt,
            target_file=filename,
        )