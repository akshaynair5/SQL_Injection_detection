# SQL Injection Detector

A Python library to detect SQL injection attempts using machine learning.

## Installation

```bash
pip install sql_injection_detector

from sql_injection_detector.detector import SQLInjectionDetector

detector = SQLInjectionDetector()
detector.load_model()
result = detector.predict("SELECT * FROM users WHERE user_id = 1 OR 1=1")
print("Prediction:", result)

