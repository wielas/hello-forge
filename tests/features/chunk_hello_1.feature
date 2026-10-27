Feature: Greeting
  The package can greet a named person.

  Scenario: greet a name
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
