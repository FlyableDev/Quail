import json
import os
from functools import wraps

from rich.style import Style

from cli.cli_types import QuailSuiteTestNameType, QuailTestNameType
from utils.trim import trim
import setup.quail_setup as cli_setup

import click
from subprocess import Popen
from cli.cli_utils import console, print_quail_err

print = console.print

FLYABLE_VERSION: str
HELP = "Welcome to the Quail maker helper!"

INITIALIZED = False


def print_happy(msg: str):
    print(msg, end=" ")
    print("\\(^ v ^)/", style=Style(color="blue"))


def init_if_not_init(ctx, param, value):
    global FLYABLE_VERSION
    global INITIALIZED
    if not INITIALIZED:
        INITIALIZED = cli_setup.setup_quail()
        if INITIALIZED:
            FLYABLE_VERSION = "v0.1a1"
        else:
            ctx.abort()


@click.group(help=HELP)
def cli():
    pass


@cli.command(name="run")
@click.option(
    "--init-quail",
    is_flag=True,
    callback=init_if_not_init,
    expose_value=False,
    is_eager=True,
    help="*ignore this option*",
)
@click.argument("test", default="~")
@click.option(
    "--unit",
    "-u",
    "mode",
    flag_value="unit",
    help="Use this flag to run a unit test",
)
@click.option(
    "--integration",
    "-i",
    "mode",
    flag_value="integration",
    help="Use this flag to run an integration test",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Verbose mode",
)
def run(test, mode, verbose):
    if mode == "unit":
        process = Popen(["pytest", f"./tests/unit_tests{'/' + test if test != '~' else ''}"])
        process.communicate()

    elif mode == "integration":
        from quail.integration.integration_test import load_integration_tests
        from quail.integration.integration_test_runner import IntegrationTestRunner

        tests = load_integration_tests(
            f"./tests/integration_tests{'/' + test if test != '~' else ''}"
        )
        if verbose:
            print(tests)
        runner = IntegrationTestRunner()
        runner.add_tests(*tests)
        runner.run_all_tests()

    else:
        print_quail_err("You must add -u (unit test) or -i (integration test) before the name of your test suite.")


@cli.command(name="new")
@click.option(
    "--init-quail",
    is_flag=True,
    callback=init_if_not_init,
    expose_value=False,
    is_eager=True,
    help="*ignore this option*",
)
@click.argument("name")
@click.option(
    "--blank",
    is_flag=True,
    help="Doesn't add a placeholder test in the test suite.",
    prompt="Do you want to add a placeholder test?",
    default=True,
)
@click.option(
    "--git-add",
    is_flag=True,
    help="Adds the files created to git",
    prompt="Do you want to add the file created to git?",
    default=False,
)
def create_new_quail_integration_test(name: str, blank: bool, git_add: bool):
    """
    For more information, write `Quail new --help`\n
    Creates a new Quail test suite <x> containing a folder with a quailt_<x>.py file and a test_<x>.py file.
    """
    path = f"./tests/unit_tests/{name}"
    try:
        os.makedirs(path, exist_ok=False)
    except OSError:
        print(
            f"The Quail test suite '{name}' already exists, if you wanted to add a new test, "
            f"use the 'add' command"
        )
        return
    with open(f"{path}/quailt_{name}.py", "w+") as body:
        msg = f'"""Module {name}"""\n\n'
        if blank:
            # TODO add => Quail-macro:wrap-func test
            msg += (
                    trim(
                        f'''
                    # Quail-test:new
                    """
                    Name: YOUR_NAME
                    : {FLYABLE_VERSION}
                    Description: YOUR_DESCRIPTION
                    """
                    # Quail-test:start
                    "hello world!" == "hello world!"  # Quail-assert: True
                    
                    # Quail-test:end
                    '''
                    )
                    + "\n"
            )
        body.write(msg)

    with open(f"{path}/test_{name}.py", "w+") as body:
        body.write(
            trim(
                """
                from tests.unit_tests.conftest import quail_runtimes_tester

                @quail_runtimes_tester
                def test_runtimes():
                    pass
                """
            )
            + "\n"
        )
    if git_add:
        Popen(f"git add ./{path}")
    print_happy(f"Quail test suite {name!r} created successfully!")


is_compile = False


def get_is_compile():
    return is_compile


def set_is_compile(_ctx, _self, choice):
    global is_compile
    if choice is None:
        return
    is_compile = choice == "compile"
    print(is_compile)


@cli.command(name="add")
@click.option(
    "--init-quail",
    is_flag=True,
    callback=init_if_not_init,
    expose_value=False,
    is_eager=True,
    help="*ignore this option*",
)
@click.argument("test-suite-name", type=QuailSuiteTestNameType())
@click.option(
    "--test-name", prompt="Enter the name of your test", type=QuailTestNameType()
)
@click.option(
    "--mode",
    prompt="Enter the mode",
    default="runtime",
    type=click.Choice(["runtime", "compile", "both"]),
    callback=set_is_compile,
)
@click.option(
    "--add-tester",
    is_flag=True,
    prompt="Add a quail tester?",
    default=get_is_compile,
)
def add_test_to_test_suite(
        test_suite_name: str,
        test_name: str,
        mode: str = None,
        add_tester: bool = False,
):
    """
    For more information, write `Quail add --help`\n
    Adds a new Quail test to an already existing Quail test suite.
    """
    test_name = test_name.strip()
    if not test_name.replace("_", "").isalnum():
        print(
            f"Invalid test name {test_name!r}. Test names must be alpha numerical (though _ are allowed)"
        )
        return
    path = f"./tests/unit_tests/{test_suite_name}"
    if not os.path.exists(path):
        print(
            f"The Quail test suite '{test_suite_name}' doesn't exist, if you wanted to create a new test suite, "
            f"use the 'new' command"
        )
        return

    with open(f"{path}/quailt_{test_suite_name}.py", "a+") as body:
        msg = (
                trim(
                    f'''
                \n\n
                # Quail-test:new {mode if mode != "runtime" else ""}
                """
                Name: {test_name}
                Flyable-version: {FLYABLE_VERSION}
                Description: tests {test_name.replace("_", " ")}
                """
                # Quail-test:start
                
                # Quail-test:end
                '''
                )
                + "\n"
        )
        body.write(msg)

    if add_tester:
        with open(f"{path}/test_{test_suite_name}.py", "a+") as body:
            args = (
                "quail_test: QuailTest, stdout: StdOut"
                if mode != "compile"
                else "quail_results: CompilerResult"
            )
            body.write(
                trim(
                    f"""
                    \n\n
                    @quail_tester
                    def test_{test_name}({args}):
                        pass
                    """
                )
                + "\n"
            )
    print_happy(
        f"Quail test {test_name!r} created successfully in {test_suite_name!r}!"
    )


@cli.command(name="integration")
@click.option(
    "--init-quail",
    is_flag=True,
    callback=init_if_not_init,
    expose_value=False,
    is_eager=True,
    help="*ignore this option*",
)
@click.argument("name")
@click.option(
    "--conf",
    is_flag=True,
    help="Puts nothing in the default quail.config.json",
    prompt="Do you want to create a default config file?",
    default=True,
)
@click.option(
    "--git-add",
    is_flag=True,
    help="Adds the files created to git",
    prompt="Do you want to add the file created to git?",
    default=False,
)
def create_new_quail_integration_test(name: str, conf: bool, git_add: bool):
    """
    For more information, write `Quail integration --help`\n
    Creates a new Quail integration test <x> containing a folder with a src folder, output folder and quail.config.json.
    """
    path = f"./tests/integration_tests/{name}"
    try:
        os.makedirs(path, exist_ok=False)
    except OSError:
        print(f"The Quail Integration test '{name}' already exists")
        return

    os.mkdir(f"{path}/src")

    with open(f"{path}/quail.config.json", "w+") as body:
        if conf:
            content = json.dumps(
                {
                    "name": name,
                    "description": f"Quail Integration test '{name}' for the flyable compiler",
                    "main": "main.py",
                },
                indent=4,
            )
        else:
            content = "{}"
        body.write(content)

    with open(f"{path}/src/main.py", "w+") as body:
        body.write('print("Hello World!")')

    os.mkdir(f"{path}/output")
    os.mkdir(f"{path}/build")

    if git_add:
        Popen(f"git add ./{path}")
    print_happy(f"Quail integration test {name!r} created successfully!")
