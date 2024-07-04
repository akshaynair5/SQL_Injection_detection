import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='sql_injection_detector.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_detection(query, prediction):
    logging.info(f"Query: {query} | Prediction: {prediction}")

def generate_report():
    with open('sql_injection_detector.log', 'r') as f:
        report = f.read()
    return report