import pytest
from src.ecg_analyzer import ECGAnalyzer
from src.blood_pressure import BloodPressureMonitor
from src.pulse_oximeter import PulseOximeter
from src.models.patient import Patient

class TestDiagnosticsIntegration:
    @pytest.fixture
    def diagnostic_suite(self):
        class Suite:
            def __init__(self):
                self.ecg = ECGAnalyzer()
                self.bp = BloodPressureMonitor()
                self.spo2 = PulseOximeter()
        return Suite()
    
    @pytest.fixture
    def critical_patient(self):
        return Patient(id="CRIT-001", name="Critical", age=65)
    
    def test_critical_patient_assessment(self, diagnostic_suite, critical_patient):
        # Simulate critical readings
        ecg_result = diagnostic_suite.ecg.analyze_ecg([1.5, 0.1, 1.7, 0.2]*10, critical_patient)
        bp_result = diagnostic_suite.bp.measure_bp(170, 110, critical_patient)
        spo2_result = diagnostic_suite.spo2.measure_spo2(88, 120, critical_patient)
        
        # Verify all systems flag critical status
        assert ecg_result['rhythm'] != 'normal'
        assert "Stage 2" in bp_result['category']
        assert "Hypoxemia" in spo2_result['status']
        
        # Verify patient ID is consistently tracked
        assert ecg_result['patient_id'] == bp_result['patient_id'] == spo2_result['patient_id']