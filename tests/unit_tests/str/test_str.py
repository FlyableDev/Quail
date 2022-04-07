from quail.testers.compiler_tester import CompilerResult
from utils.utils import StdOut
from tests.unit_tests.conftest import quail_runtimes_tester, quail_tester


@quail_runtimes_tester(strict=True)
def test_runtimes():
    pass


@quail_tester
def test_concatenation(quail_results: CompilerResult, stdout: StdOut):
    """"""
    a = None
    print(a.__name__)
    # assert quail_results.func("abc").has_impl((str, ), None)
