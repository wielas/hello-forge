"""BDD steps for CHUNK-HELLO-1."""

from pytest_bdd import given, parsers, scenarios, then, when

from hello_forge.greet import greet

scenarios("../features/chunk_hello_1.feature")


@given("the package is installed", target_fixture="pkg")
def pkg():
    return greet


@when(parsers.parse('I greet "{name}"'), target_fixture="greeting")
def greeting(pkg, name):
    return pkg(name)


@then(parsers.parse('I get "{expected}"'))
def got_greeting(greeting, expected):
    assert greeting == expected
