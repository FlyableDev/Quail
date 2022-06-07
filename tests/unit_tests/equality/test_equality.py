import pytest
from tests.unit_tests.conftest import quail_tester
from quail.utils.utils import StdOut
from quail.quail_test import QuailTest

@quail_tester
def test_float_equality(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
@pytest.mark.depends_on("subtraction", "division")
def test_bool_equality(quail_test: QuailTest, stdout: StdOut):
    """bool_equality"""
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_triple_equality(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_is_operator(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_zero_and_one_bool_comparison_with_is(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_zero_and_one_bool_comparison_with_equal(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)