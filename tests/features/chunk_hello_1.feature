Feature: Greet by name
  The package returns a greeting for a provided name.

  Scenario: greet a name
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
