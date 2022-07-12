from __future__ import annotations
import asyncio, flyable
import importlib
from time import sleep

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from quail.utils.utils import StdOut
    from typing import Literal

from dataclasses import dataclass, field

from quail.constants import QUAIL_VALID_INFOS


@dataclass
class QuailTest:
    file_name: str
    mode: Literal["compile", "runtime", "both"] = "runtime"
    infos: dict[str, str] = field(default_factory=dict)
    lines: list[str] = field(default_factory=list)
    original_lines: list[str] = field(default_factory=list)

    temp_working_dir: str = field(default=None)

    def __post_init__(self):
        self.temp_working_dir += "/generated_scripts"

    def is_valid_or_raise(self):
        for info, required in QUAIL_VALID_INFOS.items():
            if not required:
                continue
            if info not in self.infos:
                raise AttributeError(
                    f"Missing {info!r}. Each test must have: \n"
                    f"{repr(QUAIL_VALID_INFOS).replace('True', '[Required]').replace('False', '[Optional]')}"
                )

    def py_compile(self):
        return compile("".join(self.lines), self.file_name, "exec")

    def fly_exec(self, stdout: StdOut):
        self.lines.insert(0, "from flyable import flyable\n")
        self.lines.insert(1, "flyable.run()\n")

        with open("_quail_test.py", "w") as f:
            f.truncate(0)
            f.writelines(self.lines)
        import _quail_test
        importlib.reload(_quail_test)
        #exec(self.py_compile(), {"built" : __builtins__, "asyncio": asyncio, "flyable": flyable}, { "asyncio": asyncio, "flyable": flyable})
        timeout = self.infos.get('Timeout', None)
        if timeout is not None:
            sleep(float(timeout))
        result = stdout.content
        if result.startswith("now running flyable engine\n"):
            result = result.replace("now running flyable engine\n", "", 1)
        stdout.clear()
        self.lines = self.lines[2:]
        return result
        """
        link_path = constants.LINKER_EXEC if platform.system() == "Windows" else "gcc"
        linker_args = [link_path, "-flto", constants.PYTHON_3_11_PATH, "output.o"]
        if platform.system() == "Windows":
            linker_args.append(constants.PYTHON_3_11_DLL_PATH)

        p0 = Popen(linker_args, cwd=self.temp_working_dir)
        p0.wait()
        if p0.returncode != 0:
            raise CompilationError("Linking error")

        linker_args = [link_path, "-flto", constants.PYTHON_3_11_PATH, "output.o"]
        if platform.system() == "Windows":
            linker_args.append(constants.PYTHON_3_11_DLL_PATH)
        p = Popen(
            [
                self.temp_working_dir + f"/a.exe",
                f"{self.temp_working_dir}/{self.name}.py",
            ],
            cwd=os.path.dirname(PYTHON_PATH),
            stdout=PIPE,
            text=True,
        )

        if isinstance(p, str):
            raise CompilationError(p)
        print(p.communicate()[0], end="")
        result = stdout.content
        stdout.clear()
        return result
        """

    def py_exec(self, stdout: StdOut):
        with open("_quail_test.py", "w") as f:
            f.truncate(0)
            f.writelines(self.lines)
        import _quail_test
        importlib.reload(_quail_test)
        #exec(self.py_compile(), {"built" : __builtins__, "asyncio": asyncio, "flyable": flyable}, { "asyncio": asyncio, "flyable": flyable})
        result = stdout.content
        stdout.clear()
        if not all(x == "True" for x in result.split("\n") if x):
            raise Warning(result)
        """exec(self.py_compile(), {"built" : __builtins__, "asyncio": asyncio}, { "asyncio": asyncio})
        result = stdout.content
        stdout.clear()
        """
        return result

    @property
    def name(self):
        return self.infos["Name"]

    @property
    def flyable_version(self) -> str:
        return self.infos["Flyable-version"]
