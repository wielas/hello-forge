Feature: Hello greet
  The greet function returns a friendly greeting.

  Scenario: Greet someone by name
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
