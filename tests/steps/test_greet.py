"""BDD steps for greeting a name."""

from pytest_bdd import given, scenarios, then, when

from hello_forge.greet import greet

scenarios("../features/chunk_hello_1.feature")


@given("the package is installed", target_fixture="package_is_installed")
def package_is_installed():
    """Confirm the installed package can be imported."""
    return greet


@when('I greet "Forge"', target_fixture="greeting")
def greet_forge(package_is_installed):
    return package_is_installed("Forge")


@then('I get "Hello, Forge!"')
def get_greeting(greeting):
    assert greeting == "Hello, Forge!"
