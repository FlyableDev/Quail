"""
Sets up Quail and checks if something is missing during installation
"""

import os
import sys
from rich import get_console
from rich.style import Style
import yaml
import importlib.util as imp_util

console = get_console()
QUAIL_ERROR_STYLE = Style(color="red")


def print_quail_err(error_msg: str, error_name: str = "Error"):
    console.print(f"Quail {error_name}: {error_msg}", style=QUAIL_ERROR_STYLE)


__CONFIG: dict = {}


def __load_flyable():
    flyable_path: str = __CONFIG["config"]["FLYABLE_DIR"]
    sys.path.append(flyable_path)
    try:
        import flyable
        return True
    except ImportError:
        return False


def __setup(config_file: str) -> bool:
    global __CONFIG
    with open(config_file, "r") as f:
        __CONFIG = yaml.full_load(f)
    if not len(__CONFIG):
        return False
    return __load_flyable()



def setup_quail(setup_file_path: str = "quail.setup.yaml") -> bool:
    if not os.path.exists(setup_file_path):
        print_quail_err(f"Required setup file {setup_file_path!r} was not found.")
        return False
    else:
        result = __setup(setup_file_path)
        if result:
            console.print("Quail is ready to go!", style="green")
        else:
            print_quail_err(f"Error loading flyable")
    return result
