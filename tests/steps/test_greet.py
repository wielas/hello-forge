"""BDD scenario for greeting a name."""

from pytest_bdd import given, scenarios, then, when

import hello_forge
from hello_forge.greet import greet

scenarios("../features/chunk_hello_1.feature")


@given("the package is installed", target_fixture="pkg")
def pkg():
    return hello_forge


@when('I greet "Forge"', target_fixture="greeting")
def greeting(pkg):
    return greet("Forge")


@then('I get "Hello, Forge!"')
def get_greeting(greeting):
    assert greeting == "Hello, Forge!"
