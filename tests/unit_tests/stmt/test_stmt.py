from tests.unit_tests.conftest import quail_runtimes_tester

@quail_runtimes_tester
def test_runtimes():
    pass

"""

CURRENTLY OUTDATED

@quail_tester
def test_func_creation(quail_results: CompilerResult):
    quail_results.assert_func("func_no_args") \
        .matches_args_format() \
        .supports_vec_calls()
        
    quail_results.assert_func("func_return") \
        .supports_tp_calls() \
        .matches_args_format(("a", "string"), ("b", "boolean"), ("c", "int"))


@quail_tester
def test_variable(quail_results: CompilerResult):
    quail_results.assert_var("b").is_of_type(list)

"""