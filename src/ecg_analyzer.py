from typing import List ,Dict
from .models.patient import Patient

class ECGAnalyzer():
    def __init__(self):
        self.norm_hr_range = (60,100)
        self.abnormal_rhythms = ['afib','bradycardia']
        
    def analyze_ecg(self, ecg_data: list[float],patient:Patient) -> Dict:
        heart_rate  = self._calculate_heart_rate(ecg_data)
        rhythm = self._detect_rhythm(ecg_data)
        return {
            'heart_rate': heart_rate,
            'rhythm': rhythm,
            'interpretation': self._interpret_results(heart_rate, rhythm, patient.age),
            'patient_id': patient.id
        }
        
    def _calculate_heart_rate(self, ecg_data:List[float]) -> float:
        if len(ecg_data) > 20:
            return 70.0
        return 60.0
    
    def _detect_rhythm(self,ecg_data: List[float]) -> str:
        try:
            variation = max(ecg_data) - min(ecg_data)
            if variation > 1.5:
                return 'afib'
            elif variation <0.3:
                return 'bradycardia'
            return 'normal'
        except ValueError as e:
            raise ValueError("Invalid ECG data") from e
    
    def _interpret_results(self, hr:float, rhythm:str, age: int) -> str:
        age_adjusted_min = max(60,70 - (age //2))
        age_adjusted_max = max(100, 80 +(age //3))
        
        if hr < age_adjusted_min:
            return "bradycardia detected" 
        elif hr > age_adjusted_max:
            return "Tachycardia detected"
        return "Normal Sinus Rhythm"
        