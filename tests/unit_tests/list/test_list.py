from quail.quail_test import QuailTest
from tests.unit_tests.conftest import quail_runtimes_tester, quail_tester
from quail.utils.utils import StdOut


@quail_runtimes_tester(exclude=["compile_list"])
def test_runtimes():
    pass

"""

CURRENTLY OUTDATED

@quail_tester
def test_compile_list(quail_results: QuailTest, stdout: StdOut):
    pass
"""