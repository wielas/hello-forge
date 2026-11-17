Feature: Greet a name
  Scenario: greet Forge
    Given the package is installed
    When I greet "Forge"
    Then I get "Hello, Forge!"
