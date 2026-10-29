"""Steps for the greeting scenario."""

from pytest_bdd import given, parsers, scenarios, then, when

import hello_forge

scenarios("../features/chunk_hello_1.feature")


@given("the package is installed", target_fixture="pkg")
def pkg():
    return hello_forge


@when(parsers.parse('I greet "{name}"'), target_fixture="greeting")
def greeting(pkg, name):
    return pkg.greet(name)


@then(parsers.parse('I get "{expected}"'))
def is_expected_greeting(greeting, expected):
    assert greeting == expected
