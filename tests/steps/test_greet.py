"""BDD steps for greeting someone."""

from pytest_bdd import given, scenarios, then, when

from hello_forge.greet import greet

scenarios("../features/chunk_hello_1.feature")


@given("the package is installed")
def package_is_installed():
    pass


@when('I greet "Forge"', target_fixture="greeting")
def greeting():
    return greet("Forge")


@then('I get "Hello, Forge!"')
def got_greeting(greeting):
    assert greeting == "Hello, Forge!"
