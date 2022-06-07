import os
from quail.integration.integration_test import load_integration_tests
from quail.integration.integration_test_runner import IntegrationTestRunner


def run_tests():
    tests = load_integration_tests(os.path.abspath(os.getcwd()))
    test_runner = IntegrationTestRunner()
    for test in tests:
        if test.name == "primes":
            test_runner.add_tests(test)

    test_runner.run_all_tests()


if __name__ == "__main__":
    run_tests()
