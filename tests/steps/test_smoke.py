"""Smoke steps — proves the pytest-bdd plumbing before any real chunk."""

import re

from pytest_bdd import given, scenarios, then, when

import hello_forge
from hello_forge.greet import greet

scenarios("../features/smoke.feature")
scenarios("../features/chunk_hello_1.feature")


@given("the package is installed", target_fixture="pkg")
def pkg():
    return hello_forge


@when("I read its version", target_fixture="version")
def version(pkg):
    return pkg.__version__


@then("it is a semver string")
def is_semver(version):
    assert re.fullmatch(r"\d+\.\d+\.\d+", version)


@when('I greet "Forge"', target_fixture="greeting")
def greeting():
    return greet("Forge")


@then('I get "Hello, Forge!"')
def got_greeting(greeting):
    assert greeting == "Hello, Forge!"
