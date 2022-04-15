from quail.quail_test import QuailTest
from tests.unit_tests.conftest import quail_runtimes_tester, quail_tester
from utils.utils import StdOut


@quail_runtimes_tester
def test_runtimes():
    pass

@quail_tester
def test_list_len(quail_test: QuailTest, stdout: StdOut):
    pass


@quail_tester
def test_compile_list(quail_results: QuailTest, stdout: StdOut):
    pass
