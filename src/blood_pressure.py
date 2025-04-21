from .models.patient import Patient
from typing import Dict, Tuple

class BloodPressureMonitor:
    CATEGORIES = {
        (0, 90): "Hypotension",
        (90, 120): "Normal",
        (120, 140): "Elevated",
        (140, 160): "Hypertension Stage 1",
        (160, 180): "Hypertension Stage 2",
        (180, 300): "Hypertensive Crisis"
    }
    
    def __init__(self):
        self.calibration_factor = 1.0
    
    def calibrate(self, factor: float):
        if not 0.8 <= factor <= 1.2:
            raise ValueError("Calibration factor must be between 0.8 and 1.2")
        self.calibration_factor = factor
    
    def measure_bp(self, systolic: int, diastolic: int, patient: Patient) -> Dict:
        if systolic <= 0 or diastolic <= 0:
            raise ValueError("Blood pressure values must be positive")
        
        if systolic < diastolic:
            raise ValueError("Systolic must be greater than diastolic")
        
        adjusted_sys = int(systolic * self.calibration_factor)
        adjusted_dia = int(diastolic * self.calibration_factor)
        
        return {
            'systolic': adjusted_sys,
            'diastolic': adjusted_dia,
            'category': self._categorize_bp(adjusted_sys, adjusted_dia),
            'patient_id': patient.id,
            'age_considered': self._consider_age(adjusted_sys, adjusted_dia, patient.age)
        }
    
    def _categorize_bp(self, systolic: int, diastolic: int) -> str:
        for (min_sys, max_sys), category in self.CATEGORIES.items():
            if min_sys <= systolic < max_sys:
                return category
        return "Uncategorized"
    
    def _consider_age(self, systolic: int, diastolic: int, age: int) -> bool:
        if age < 18:
            return systolic > 120 or diastolic > 80
        elif age > 60:
            return systolic > 140 or diastolic > 90
        return systolic > 130 or diastolic > 85