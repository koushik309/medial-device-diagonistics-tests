Feature: ECG Analysis
  As a cardiologist
  I want to analyze ECG data
  So that I can diagnose cardiac conditions

  Scenario Outline: Detect abnormal rhythms
    Given a patient "<name>" aged <age> with ID "<id>"
    And the following ECG data points <ecg_data>
    When I analyze the ECG
    Then the rhythm should be "<expected_rhythm>"
    And the interpretation should contain "<expected_interpretation>"

    Examples:
      | name      | age | id      | ecg_data                          | expected_rhythm | expected_interpretation |
      | Jane Doe  | 60  | PT-002  | [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]    | bradycardia     | Bradycardia detected    |
      | Mike Smith| 35  | PT-003  | [1.5, 0.1, 1.7, 0.2, 1.6, 0.3]    | afib            | Abnormal rhythm        |