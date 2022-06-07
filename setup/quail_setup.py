"""
Sets up Quail and checks if something is missing during installation
"""

import os
import sys
import time

from rich import get_console
from rich.style import Style
import yaml

from setup import constants

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


def __load_python_path():
    python_path: str = __CONFIG["config"]["PYTHON_PATH"]
    constants.set_python_path(python_path)
    return True


def __setup(config_file: str) -> bool:
    global __CONFIG
    with open(config_file, "r") as f:
        __CONFIG = yaml.full_load(f)
    if not len(__CONFIG):
        return False
    return all((__load_flyable(), __load_python_path()))


def setup_quail(
        setup_file_path: str = "quail.setup.yaml",
        example_setup_file_path="quail.setup.example.yaml",
) -> bool:
    if not os.path.exists(setup_file_path):
        print_quail_err(f"Required setup file {setup_file_path!r} was not found.")
        console.print("Trying to create it from quail.setup.example.yaml...")
        if not os.path.exists(example_setup_file_path):
            print_quail_err(
                f"An error occurred while creating {setup_file_path!r} from {example_setup_file_path!r}. "
                f"{example_setup_file_path!r} does not exist."
            )
            return False
        time.sleep(1)
        with open(example_setup_file_path, "r") as example_setup_file:
            lines = example_setup_file.readlines()
        with open(setup_file_path, "w+") as setup_file:
            setup_file.writelines(lines)
        return setup_quail(setup_file_path, example_setup_file_path)
    else:
        result = __setup(setup_file_path)
        if result:
            console.print("Quail is ready to go!", style="green")
        else:
            print_quail_err(f"Error loading flyable")
    return result
