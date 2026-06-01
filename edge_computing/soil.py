import numpy as np
import json
from typing import Dict
from dataclasses import dataclass

@dataclass
class SoilSample:
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    organic_carbon: float

class SoilAnalyzer:
    def __init__(self):
        # Load model weights (mock)
        self.model_weights = np.array([0.4, 0.3, 0.2, 0.05, 0.05])
        self.thresholds = {
            'nitrogen': (30, 50),
            'phosphorus': (15, 40),
            'potassium': (20, 50)
        }

    def analyze(self, sample: SoilSample) -> Dict:
        """Comprehensive soil analysis"""
        features = np.array([
            sample.nitrogen,
            sample.phosphorus,
            sample.potassium,
            sample.ph,
            sample.organic_carbon
        ])
        
        # Calculate fertilizer requirement
        recommendation = np.dot(features, self.model_weights)
        
        # Generate Hindi report
        report = {
            'hindi_report': (
                f"मिट्टी विश्लेषण:\n"
                f"नाइट्रोजन: {sample.nitrogen} ppm ({self._get_status(sample.nitrogen, 'nitrogen')})\n"
                f"फॉस्फोरस: {sample.phosphorus} ppm\n"
                f"सुझाव: {max(0, 50-sample.nitrogen):.1f} kg यूरिया/एकड़"
            ),
            'english_report': str(sample),
            'recommendation': float(recommendation)
        }
        
        return report

    def _get_status(self, value: float, nutrient: str) -> str:
        low, high = self.thresholds[nutrient]
        if value < low:
            return "कम"
        elif value > high:
            return "अधिक"
        return "सामान्य"

if __name__ == "__main__":
    # Mock sensor data
    sample = SoilSample(
        nitrogen=35.0,
        phosphorus=20.0,
        potassium=40.0,
        ph=6.5,
        organic_carbon=0.8
    )
    
    analyzer = SoilAnalyzer()
    result = analyzer.analyze(sample)
    print(json.dumps(result, indent=2, ensure_ascii=False))