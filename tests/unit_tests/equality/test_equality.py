import pytest

from quail.quail_test import QuailTest
from utils.utils import StdOut
from tests.unit_tests.conftest import quail_runtimes_tester, quail_tester


@quail_runtimes_tester
def test_runtimes():
    pass


@quail_tester
@pytest.mark.depends_on("subtraction", "division")
def test_bool_equality(quail_test: QuailTest, stdout: StdOut):
    """bool_equality"""
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)


