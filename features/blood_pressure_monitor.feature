Feature: Blood Pressure Monitoring
  As a nurse
  I want to monitor patient blood pressure
  So that I can identify hypertension or hypotension

  Scenario: Normal blood pressure reading
    Given a blood pressure monitor
    And a patient "Sarah Connor" aged 30 with ID "PT-004"
    When I measure blood pressure of 115/75
    Then the adjusted reading should be 115/75
    And the category should be "Normal"
    And age consideration should be False

  Scenario: Calibrated hypertension reading
    Given a blood pressure monitor calibrated with factor 1.1
    And a patient "John Connor" aged 65 with ID "PT-005"
    When I measure blood pressure of 130/85
    Then the adjusted reading should be 143/94
    And the category should be "Hypertension Stage 1"
    And age consideration should be True