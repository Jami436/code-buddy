from rich.console import Console
from rich.prompt import Prompt

from agents.refactor_agent import create_code_agent

from utils.printer import print_response
from utils.response_parser import extract_text
from utils.errors import handle_exception
from utils.command_handler import CommandHandler

from tools.file_manager import write_file_content
from utils.code_parser import extract_code

console = Console()


def main():
    agent = create_code_agent()
    handler = CommandHandler()

    config = {
        "configurable": {
            "thread_id": "default"
        }
    }

    while True:
        query = Prompt.ask("\n[bold green]You[/bold green]")

        # Default value in case the input isn't a command
        command_result = None

        try:
            command_result = handler.handle(query)

            # Local command
            if command_result.handled:

                # Commands like /help, /files, /read
                if command_result.ai_prompt is None:
                    continue

                # Commands like /analyze or /refactor
                query = command_result.ai_prompt

            with console.status("[bold cyan]Thinking...[/bold cyan]"):
                result = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": query,
                            }
                        ]
                    },
                    config=config,
                )

            response = extract_text(result)
            print_response(response)

            # Only /refactor returns a target_file
            if (
                command_result is not None
                and command_result.target_file is not None
            ):
                answer = Prompt.ask(
                    "\n[bold yellow]Apply these changes? (y/n)[/bold yellow]",
                    default="n",
                ).strip().lower()

                if answer == "y":
                    clean_code = extract_code(response)

                    write_result = write_file_content(
                        command_result.target_file,
                        clean_code,
                    )

                    console.print(
                        f"[bold green]✔ {write_result}[/bold green]"
                    )

                else:
                    console.print(
                        "[yellow]Changes discarded.[/yellow]"
                    )

        except Exception as e:
            handle_exception(e)


if __name__ == "__main__":
    main()