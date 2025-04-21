from .models.patient import Patient
from typing import Dict

class PulseOximeter:
    def __init__(self):
        self.altitude_adjustment = 0
    
    def set_altitude(self, meters: int):
        if meters < 0:
            raise ValueError("Altitude cannot be negative")
        self.altitude_adjustment = meters // 1000  # 1% per 1000m
    
    def measure_spo2(self, spo2: int, pulse: int, patient: Patient) -> Dict:
        if not 0 <= spo2 <= 100:
            raise ValueError("SpO2 must be between 0-100%")
        
        if pulse <= 0:
            raise ValueError("Pulse must be positive")
        
        adjusted_spo2 = spo2 - self.altitude_adjustment
        
        return {
            'spo2': adjusted_spo2,
            'pulse': pulse,
            'status': self._determine_status(adjusted_spo2, pulse, patient.age),
            'patient_id': patient.id
        }
    
    def _determine_status(self, spo2: int, pulse: int, age: int) -> str:
        if spo2 < 90:
            return "Hypoxemia - Seek medical attention"
        elif spo2 < 94:
            return "Borderline low - Monitor closely"
        
        max_normal_pulse = 220 - age
        if pulse > max_normal_pulse * 0.9:
            return "Elevated pulse rate"
        
        return "Normal"