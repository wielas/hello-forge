Feature: Greet someone
  Scenario: greet a named person
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
