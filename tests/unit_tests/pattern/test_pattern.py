from tests.unit_tests.conftest import quail_tester
from quail.utils.utils import StdOut
from quail.quail_test import QuailTest

@quail_tester
def test_MatchValue(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchSingleton(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchSequence(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchMapping(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchClass(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchStar(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchAs(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)

@quail_tester
def test_MatchOr(quail_test: QuailTest, stdout: StdOut):
    assert quail_test.fly_exec(stdout) == quail_test.py_exec(stdout)
