from tests.unit_tests.conftest import quail_tester
from quail.utils.utils import StdOut
from quail.quail_test import QuailTest


@quail_tester
def test_addition(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)


@quail_tester
def test_subtraction(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)


@quail_tester
def test_multiplication(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)


@quail_tester
def test_division(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

""" FIXME : FIX try except
@quail_tester
def test_division_by_zero(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)
"""

@quail_tester
def test_modulo(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)


@quail_tester
def test_pow(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_floor_division(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_LShift(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_BitAnd(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_BitOr(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_BitXor(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatMul(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)