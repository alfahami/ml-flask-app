from flask import Flask, request, render_template, jsonify, url_for
from utils import clean_text
import pickle
import time
import os

app = Flask(__name__)

MODEL_VERSION = 'model_V0.pkl'
VECTORIZER_VERSION = 'vectorizer_V0.pkl'

# Chargement des models
vectorizer_path = os.path.join(os.getcwd(), 'model_assets', VECTORIZER_VERSION)
model_path = os.path.join(os.getcwd(), 'model_assets', MODEL_VERSION)
vectorizer = pickle.load(open(vectorizer_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))



@app.route('/', methods=['GET'])
def index_view():
    return render_template('index.html')

@app.route('/sof-dataviz', methods=['GET'])
def dataviz_view():
    return render_template('sof-dataviz.html')

@app.route('/troll-notebook', methods=['GET'])
def troll_notebook():
    return render_template('model_dev.html')

@app.route('/cyber-troll', methods=['GET', 'POST'])
def troll_view():

    if request.method == 'POST':

        response = request.form['text']
        input_text = clean_text(response)
        input_text = vectorizer.transform([input_text])
        prediction = model.predict(input_text)
        prediction = 'Cyber-Troll' if prediction[0] == 1 else 'Non Cyber-Troll'
        return render_template('cyber-troll.html', text=prediction, submission=response)
    else:
        return render_template('cyber-troll.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        response = request.form['text']
        input_text = clean_text(response)
        input_text = vectorizer.transform([input_text])
        prediction = model.predict(input_text)
        prediction = 'Cyber-Troll' if prediction[0] == 1 else 'Non Cyber-Troll'
        return render_template('cyber-troll.html', text=prediction, submission=response)
    else:
        return render_template('cyber-troll.html')

if __name__ == '__main__':
    app.run(debug=True)
