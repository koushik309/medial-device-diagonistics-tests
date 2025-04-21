from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.ecg_analyzer import ECGAnalyzer
from src.models.patient import Patient

scenarios('../ecg_analysis.feature')

@pytest.fixture
def ecg_analyzer():
    return ECGAnalyzer()

@given(parsers.parse('a patient "{name}" aged {age} with ID "{id}"'))
def create_patient(name, age, id):
    return Patient(id=id, name=name, age=int(age))

@given(parsers.parse('the following ECG data points {ecg_data}'))
def load_ecg_data(ecg_data):
    # Convert string representation of list to actual list
    return eval(ecg_data)

@when("I analyze the ECG")
def analyze_ecg(ecg_analyzer, create_patient, load_ecg_data):
    return ecg_analyzer.analyze_ecg(load_ecg_data, create_patient)

@then(parsers.parse('the heart rate should be approximately {expected_hr}'))
def verify_heart_rate(analyze_ecg, expected_hr):
    assert pytest.approx(analyze_ecg['heart_rate'], abs=5) == float(expected_hr)

@then(parsers.parse('the rhythm should be "{expected_rhythm}"'))
def verify_rhythm(analyze_ecg, expected_rhythm):
    assert analyze_ecg['rhythm'] == expected_rhythm

@then(parsers.parse('the interpretation should be "{expected_interpretation}"'))
def verify_interpretation(analyze_ecg, expected_interpretation):
    assert analyze_ecg['interpretation'] == expected_interpretation

@then(parsers.parse('the interpretation should contain "{expected_text}"'))
def verify_interpretation_contains(analyze_ecg, expected_text):
    assert expected_text in analyze_ecg['interpretation']