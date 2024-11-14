from flask import Flask, request, jsonify

import joblib
import joblib  # or any other library you're using to load your model
import os


app = Flask(__name__)

# Load the model
model = joblib.load('Food_nutrition_analysis.pkl')

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/favicon.ico')
def favicon():
    return '', 204
# Load the machine learning model
model_path = os.path.join(os.path.dirname(__file__), 'Food_nutrition_analysis.py')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = data['input']
        prediction = model.predict([input_data])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
