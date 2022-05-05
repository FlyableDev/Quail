import json, os
import platform
from dataclasses import dataclass, field
from subprocess import Popen, PIPE
from io import StringIO
from contextlib import redirect_stdout

from flyable.compiler import Compiler
import setup.constants as constants

from utils.utils import CompilationError
import integration.constants as const


@dataclass
class IntegrationTest:
    name: str
    desc: str
    main: str
    dir_path: str

    __lines: list[str] | None = field(default=None, init=False)
    __main_path: str = field(init=False)
    __output_dir: str = field(init=False)

    def __post_init__(self):

        self.__output_dir = self.dir_path + "/build"
        self.__main_path = f"{self.dir_path}/src/{self.main if self.main.endswith('.py') else self.main + '.py'}"

    def py_compile(self):
        return compile("".join(self.lines), self.dir_path, "exec")

    @property
    def lines(self):
        if self.__lines is None:
            with open(self.__main_path, "r") as f:
                self.__lines = f.readlines()

        return self.__lines

    def fly_compile(self, save_results: bool = False):
        compiler = Compiler()
        compiler.add_file(self.__main_path)
        compiler.set_output_path(f"{self.__output_dir}/output.o")

        try:
            compiler.compile()
        except Exception as e:
            raise CompilationError(f"COMPILATION_ERROR: {e}")

        if not compiler.has_error():
            return compiler

        raise CompilationError(compiler.get_errors())

    def fly_exec(self):
        self.fly_compile()
        link_path = constants.LINKER_EXEC if platform.system() == "Windows" else "gcc"
        linker_args = [link_path, "-flto", constants.PYTHON_3_11_PATH, "output.o"]
        if platform.system() == "Windows":
            linker_args.append(constants.PYTHON_3_11_DLL_PATH)

        p0 = Popen(linker_args, cwd=self.__output_dir)
        p0.wait()
        if p0.returncode != 0:
            raise CompilationError("Linking error")

        linker_args = [link_path, "-flto", constants.PYTHON_3_11_PATH, "output.o"]
        if platform.system() == "Windows":
            linker_args.append(constants.PYTHON_3_11_DLL_PATH)
        p = Popen(
            [
                self.__output_dir + f"/a.exe",
                f"{self.__output_dir}/{self.name}.py",
            ],
            cwd=os.path.dirname(constants.PYTHON_PATH),
            stdout=PIPE,
            text=True,
        )

        if isinstance(p, str):
            raise CompilationError(p)
        result = p.communicate()[0]
        return result

    def py_exec(self):
        f = StringIO()
        with redirect_stdout(f):
            exec(self.py_compile(), {})
        s = f.getvalue()
        return s


def load_integration_tests(base_dir: str):
    if not os.path.isdir(base_dir):
        return []
    tests = []

    for test_file in os.listdir(base_dir):
        test_file_path = f"{base_dir}/{test_file}"
        if os.path.isdir(test_file_path):
            tests += load_integration_tests(test_file_path)
            continue
        if test_file == const.quail_config_file_name:
            with open(test_file_path, "r") as f:
                config_content = json.loads("".join(f.readlines()))

            if not valid_config(config_content):
                raise Exception(f"Invalid test config in {test_file} test")

            tests.append(
                IntegrationTest(
                    config_content["name"],
                    config_content["description"],
                    config_content["main"],
                    base_dir,
                )
            )

    return tests


def valid_config(config_content: dict):
    return all(key in config_content for key in const.required_keys)