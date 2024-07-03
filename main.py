import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

class SQLInjectionDetector:
    def __init__(self):
        self.vectorizer = None
        self.model = None

    def train(self, data_path):
        data = pd.read_csv(data_path)
        data.dropna(inplace=True)
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(data['Query'])
        y = data['Label']
        self.model = LogisticRegression()
        self.model.fit(X, y)
        with open('vectorizer.pkl', 'wb') as f:
            pickle.dump(self.vectorizer, f)
        with open('model.pkl', 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self):
        with open('vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, query):
        if self.vectorizer is None or self.model is None:
            raise Exception("Model not loaded.")
        query_vectorized = self.vectorizer.transform([query])
        prediction = self.model.predict(query_vectorized)
        return prediction[0]