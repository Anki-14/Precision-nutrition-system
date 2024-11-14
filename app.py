from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load the model using pickle
model_path = os.path.join(os.path.dirname(__file__), 'Food_nutrition_analysis.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the POST request
        data = request.get_json()
        input_data = data['input']

        # Make prediction using the model
        prediction = model.predict([input_data])

        # Return prediction result as JSON response
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        # Return error message in case of failure
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
