from rich.console import Console
from rich.prompt import Prompt

from agents.refactor_agent import create_code_agent

from utils.printer import print_response
from utils.response_parser import extract_text
from utils.errors import handle_exception
from utils.command_handler import CommandHandler

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
        command = query.lower().strip()

        try:
            if handler.handle(command):
                continue
        except SystemExit:
            break

        try:

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
                    config=config
                )

            print_response(extract_text(result))

        except Exception as e:
            handle_exception(e)


if __name__ == "__main__":
    main()