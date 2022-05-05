from quail.quail_test import QuailTest
from quail.utils.indenter import get_first_indent


class PostQuailTestParser:
    def __init__(self, quail_test: QuailTest):
        self.quail_test = quail_test

    def post_parse(self):
        flyable_version = self.quail_test.flyable_version
        match flyable_version:
            case "v0.1a1":
                wrap_test_in_func(self.quail_test)


def wrap_test_in_func(test: QuailTest, name="_quail_test_func"):
    # adding padding to all lines

    indent = " " * 4  # get_first_indent(test.lines)
    test.lines = [indent + line for line in test.lines]

    # adding the test func at the start
    test.lines.insert(0, f"def {name}():\n")

    # adding the func call at the end
    test.lines.append(f"\n{name}()\n")