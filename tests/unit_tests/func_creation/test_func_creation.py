from tests.unit_tests.conftest import quail_runtimes_tester, quail_tester


@quail_runtimes_tester
def test_runtimes():
    pass

""" 

CURRENTLY OUTDATED

@quail_tester
def test_func_creation(quail_results: CompilerResult):
    quail_results.assert_func("abc") \
        .matches_args_format(("param1",)) \
        .supports_vec_calls() \
        .has_impl(str)
    quail_results.assert_func("gt2") \
        .supports_tp_calls() \
        .matches_args_format(("param", "int"), ("param2",))


@quail_tester
def test_variable(quail_results: CompilerResult):
    quail_results.assert_var("b").is_of_type(list)

"""