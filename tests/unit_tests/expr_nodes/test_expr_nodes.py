from tests.unit_tests.conftest import quail_runtimes_tester

@quail_runtimes_tester(exclude=["NamedExpr"])
def test_runtimes():
    pass
