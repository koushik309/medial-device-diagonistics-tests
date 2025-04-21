import pytest
from src.models.patient import Patient

# This fixture will be automatically available to ALL tests
@pytest.fixture(scope="session")
def shared_patient():
    """A patient fixture that persists for all tests"""
    return Patient(id="SHARED-001", name="Shared Patient", age=45)

# Fixture for ECG tests
@pytest.fixture
def ecg_analyzer():
    from src.ecg_analyzer import ECGAnalyzer
    return ECGAnalyzer()

# Fixture for blood pressure tests
@pytest.fixture
def bp_monitor():
    from src.blood_pressure import BloodPressureMonitor
    return BloodPressureMonitor()

# This runs before/after each test automatically
@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup code runs before each test
    print("\n=== Starting test ===")
    yield
    # Teardown code runs after each test
    print("=== Test completed ===")