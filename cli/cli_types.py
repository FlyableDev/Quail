import click


class QuailSuiteTestNameType(click.ParamType):
    name = "test_suite_name_type"

    def __init__(self):
        super().__init__()

    def convert(self, value, param, ctx):
        test_suite_name = value.strip()
        path = f"./tests/unit_tests/{test_suite_name}"
        if not os.path.exists(path):
            self.fail(
                f"The Quail test suite '{test_suite_name}' doesn't exist, if you wanted to create a new test suite, "
                f"use the 'new' command",
                param=param,
                ctx=ctx,
            )
        return test_suite_name


class QuailTestNameType(click.ParamType):
    name = "quail_test_name_type"

    def __init__(self):
        super().__init__()

    def convert(self, value, param, ctx):
        test_name = value.strip()
        if not test_name.replace("_", "").isalnum():
            self.fail(
                f"Invalid test name {test_name!r}. Test names must be alpha numerical (though _ are allowed)",
                param=param,
                ctx=ctx,
            )
        return test_name