import pytest
from src.ecg_analyzer import ECGAnalyzer
from src.models.patient import Patient

class TestECGAnalyzer:
    @pytest.fixture
    def analyzer(self):
        return ECGAnalyzer()
    
    @pytest.fixture
    def sample_patient(self):
        return Patient(id="TEST-001", name="Test Patient", age=40)
    
    def test_analyze_ecg_normal(self, analyzer, sample_patient):
        ecg_data = [0.1, 0.3, 0.8, 1.2, 0.7, 0.4, 0.2] * 10
        result = analyzer.analyze_ecg(ecg_data, sample_patient)
        
        assert 60 <= result['heart_rate'] <= 100
        assert result['rhythm'] == 'normal'
        assert "Normal" in result['interpretation']
    
    def test_analyze_ecg_empty_data(self, analyzer, sample_patient):
        with pytest.raises(ValueError) as excinfo:
            analyzer.analyze_ecg([], sample_patient)
        assert "Invalid ECG data" in str(excinfo.value)
    
    @pytest.mark.parametrize("age,expected_min_hr", [
        (20, 60), (40, 60), (60, 60), (80, 60)
    ])
    def test_age_adjusted_hr_ranges(self, analyzer, age, expected_min_hr):
        patient = Patient(id="AGE-TEST", name="Age Test", age=age)
        result = analyzer.analyze_ecg([1.0]*50, patient)
        assert result['heart_rate'] >= expected_min_hr