Feature: Greeting
  The package can greet a person by name.

  Scenario: greet a person
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
