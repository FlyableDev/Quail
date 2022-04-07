from rich import get_console
from rich.style import Style

MAIN_HELP_MSG = "Welcome to the Quail CLI helper!"

console = get_console()
QUAIL_ERROR_STYLE = Style(color="red", underline=True)
QUAIL_WARNING_STYLE = Style(color="yellow")
QUAIL_SUCCESS_STYLE = Style(color="green")
QUAIL_OK_STYLE = Style()


def print_quail_err(error_msg: str, error_name: str = "Error"):
    console.print(f"Quail ${error_msg}: ${error_msg}", style=QUAIL_ERROR_STYLE)
