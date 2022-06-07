from tests.unit_tests.conftest import quail_tester
from quail.utils.utils import StdOut
from quail.quail_test import QuailTest

@quail_tester
def test_empty_str_creation(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_str_equality(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_len_str(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_concatenation(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_unicode_str(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_contains_str(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_str_slicing(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)
