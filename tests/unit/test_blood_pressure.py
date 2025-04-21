import pytest
from src.blood_pressure import BloodPressureMonitor
from src.models.patient import Patient

class TestBloodPressureMonitor:
    @pytest.fixture
    def monitor(self):
        return BloodPressureMonitor()
    
    @pytest.fixture
    def adult_patient(self):
        return Patient(id="ADULT-001", name="Adult", age=40)
    
    @pytest.fixture
    def elderly_patient(self):
        return Patient(id="ELDERLY-001", name="Elderly", age=70)
    
    def test_calibration(self, monitor):
        monitor.calibrate(1.1)
        assert monitor.calibration_factor == 1.1
        
        with pytest.raises(ValueError):
            monitor.calibrate(0.5)
    
    @pytest.mark.parametrize("sys,dia,expected_category", [
        (85, 55, "Hypotension"),
        (110, 70, "Normal"),
        (130, 85, "Elevated"),
        (150, 95, "Hypertension Stage 1"),
        (170, 105, "Hypertension Stage 2"),
        (190, 120, "Hypertensive Crisis")
    ])
    def test_bp_categorization(self, monitor, adult_patient, sys, dia, expected_category):
        result = monitor.measure_bp(sys, dia, adult_patient)
        assert result['category'] == expected_category
    
    def test_age_consideration(self, monitor, adult_patient, elderly_patient):
        adult_result = monitor.measure_bp(135, 85, adult_patient)
        elderly_result = monitor.measure_bp(135, 85, elderly_patient)
        
        assert adult_result['age_considered'] is True
        assert elderly_result['age_considered'] is False