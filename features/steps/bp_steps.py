
from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.blood_pressure import BloodPressureMonitor
from src.models.patient import Patient

scenarios('../blood_pressure_monitor.feature')

@pytest.fixture
def bp_monitor():
    return BloodPressureMonitor()

@given("a blood pressure monitor")
def clean_bp_monitor(bp_monitor):
    bp_monitor.calibrate(1.0)
    return bp_monitor

@given(parsers.parse('a blood pressure monitor calibrated with factor {factor}'))
def calibrated_bp_monitor(bp_monitor, factor):
    bp_monitor.calibrate(float(factor))
    return bp_monitor

@given(parsers.parse('a patient "{name}" aged {age} with ID "{id}"'))
def create_patient(name, age, id):
    return Patient(id=id, name=name, age=int(age))

@when(parsers.parse('I measure blood pressure of {systolic}/{diastolic}'))
def measure_bp(bp_monitor, create_patient, systolic, diastolic):
    return bp_monitor.measure_bp(
        int(systolic), 
        int(diastolic), 
        create_patient
    )

@then(parsers.parse('the adjusted reading should be {expected_sys}/{expected_dia}'))
def verify_bp_reading(measure_bp, expected_sys, expected_dia):
    assert measure_bp['systolic'] == int(expected_sys)
    assert measure_bp['diastolic'] == int(expected_dia)

@then(parsers.parse('the category should be "{expected_category}"'))
def verify_bp_category(measure_bp, expected_category):
    assert measure_bp['category'] == expected_category

@then("age consideration should be True")
def verify_age_consideration_true(measure_bp):
    assert measure_bp['age_considered'] is True

@then("age consideration should be False")
def verify_age_consideration_false(measure_bp):
    assert measure_bp['age_considered'] is False