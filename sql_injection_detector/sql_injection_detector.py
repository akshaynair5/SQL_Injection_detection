import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import logging

# Configure logging
logging.basicConfig(filename='sql_injection_detector.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_detection(query, prediction):
    logging.info(f"Query: {query} | Prediction: {prediction}")

def generate_report():
    with open('sql_injection_detector.log', 'r') as f:
        report = f.read()
    return report

class SQLInjectionDetector:
    def __init__(self, model_path='classifier.pkl', vectorizer_path='vectorizer.pkl'):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.vectorizer = None
        self.model = None

    def load_model(self):
        with open(self.vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, query):
        if self.vectorizer is None or self.model is None:
            raise Exception("Model not loaded.")
        query_vectorized = self.vectorizer.transform([query])
        prediction = self.model.predict(query_vectorized)
        log_detection(query, prediction[0])
        return prediction[0]

# Function to predict using the saved model
def detect_sql_injection(query, model_path='classifier.pkl', vectorizer_path='vectorizer.pkl'):
    detector = SQLInjectionDetector(model_path=model_path, vectorizer_path=vectorizer_path)
    detector.load_model()
    prediction = detector.predict(query)
    return prediction

# Function to generate report
def generate_detection_report():
    return generate_report()
