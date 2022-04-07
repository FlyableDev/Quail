"""
Sets up Quail and checks if something is missing during installation
"""
import time
import os

from rich import get_console
from rich.style import Style

console = get_console()
QUAIL_ERROR_STYLE = Style(color="red")


def print_quail_err(error_msg: str, error_name: str = "Error"):
    console.print(f"Quail ${error_msg}: ${error_msg}", style=QUAIL_ERROR_STYLE)


def setup_quail(setup_file_path: str = "../quail.setup.yaml"):
    if not os.path.exists(setup_file_path):
        print_quail_err("Required setup file 'quail.setup.yaml' was not found.")
    else:
        console.print("Setting up Quail, hang in there...")
        time.sleep(1)
        console.print("Quail is ready to go!", style="green")
