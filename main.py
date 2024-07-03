from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

app = Flask(__name__)

# Load data from CSV and train model once at the start
data = pd.read_csv('SQL_Injections_Dataset.csv')
data.dropna(inplace=True)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['Query'])
y = data['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, zero_division=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def predict():
    user_text = request.form['command']
    user_text_vectorized = vectorizer.transform([user_text])
    prediction = model.predict(user_text_vectorized)

    return f'Prediction: {prediction[0]}'

if __name__ == '__main__':
    app.run(port=3030, debug=True)
