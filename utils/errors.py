from rich.console import Console
from rich.panel import Panel
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

console = Console()

def show_error(title: str, message: str):
    """Display a formatted error message."""
    console.print(
        Panel(
            message,
            title=f"[bold red]{title}[/bold red]",
            border_style="red",
        )
    )

def handle_exception(error: Exception):
    """
    Convert common exceptions into user-friendly messages.
    """

    message = str(error)

    if isinstance(error, ChatGoogleGenerativeAIError):

        if "RESOURCE_EXHAUSTED" in message:

            show_error(
                "Gemini Quota Exceeded",
                (
                    "You have reached the Gemini free-tier request limit.\n\n"
                    "Please wait for your quota to reset or use another API key."
                ),
            )

            return

        show_error("Gemini API Error", message)
        return

    if "No such file" in message:
        show_error("File Error", message)
        return

    show_error("Unexpected Error", message)