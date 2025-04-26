Feature: Validate the prime number function

  Scenario: Valid input returns correct type
    Given the input number 10
    When the function is executed
    Then the output type should be <class 'list'>

  Scenario: Zero as input
    Given the input number 0
    When the function is executed
    Then the output type should be <class 'list'>

  Scenario: Large number as input
    Given the input number 50
    When the function is executed
    Then the output type should be <class 'list'>