Medical Diagnostics Testing Framework
Python Version
Tests
Coverage

A pytest-based testing framework for validating medical diagnostic equipment software, with BDD (Behavior-Driven Development) support.

Project Overview
Tests three core medical diagnostic components:

ECG Analyzer - Heart rhythm and rate analysis

Blood Pressure Monitor - BP measurement and classification

Pulse Oximeter - Oxygen saturation monitoring

Project Structure

medical-diagnostics-tests/
├── features/            # BDD feature files
├── src/                 # Medical device implementations
├── tests/               # Unit and integration tests
├── reports/             # Test and coverage reports
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

Getting Started
Prerequisites
Python 3.8+


Installation

git clone https://github.com/koushik309/medical-diagnostics-tests.git
cd medical-diagnostics-tests
pip install -r requirements.txt


Running Tests

# Run all tests with coverage
pytest --cov=src --cov-report=html:reports/coverage

# Run specific test type
pytest tests/unit/               # Unit tests only
pytest tests/integration/        # Integration tests
pytest features/                 # BDD scenarios


Test Reports
After running tests, view reports:

Test Results: reports/report.html

Coverage: reports/coverage/index.html

Key Components
1. ECG Analyzer
Detects normal/abnormal rhythms

Age-adjusted heart rate evaluation

Example BDD scenario:

gherkin
Scenario: Detect atrial fibrillation
  Given ECG data showing irregular peaks
  When analyzed for patient aged 65
  Then flag "atrial fibrillation" alert
2. Blood Pressure Monitor
Categorizes readings (Normal → Hypertensive Crisis)

Age-specific thresholds

Calibration testing

3. Pulse Oximeter
Altitude-adjusted SpO₂ readings

Pulse rate analysis
