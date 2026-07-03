from rich.console import Console
from rich.prompt import Prompt

from agents.refactor_agent import create_code_agent

from utils.banner import show_banner
from utils.cli import show_help
from utils.printer import print_response
from utils.response_parser import extract_text
from utils.errors import handle_exception

console = Console()


def main():

    show_banner()
    show_help()

    agent = create_code_agent()

    config = {
        "configurable": {
            "thread_id": "default"
        }
    }

    while True:

        query = Prompt.ask("\n[bold green]You[/bold green]")
        command = query.lower().strip()

        if command in {"/exit", "/quit", "exit", "quit"}:
            console.print("\n Goodbye!")
            break

        if command == "/help":
            show_help()
            continue

        if command == "/clear":
            console.clear()
            show_banner()
            show_help()
            continue

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