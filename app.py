from flask import Flask, request, jsonify
import joblib  # or any other library you're using to load your model

# Create the Flask app
app = Flask(__name__)

# Load the machine learning model
model = joblib.load('C:\Users\ADMIN\OneDrive\Desktop\Precision-nutrition-system-main\Food_nutrition_analysis.py')  # Adjust the path

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json()  # This expects JSON data

        # Perform any preprocessing you need on the data (if required)
        # For example, if the data comes in as a list or dict, process it to match model input
        input_data = data['input']  # Adjust based on your input format

        # Use the model to make a prediction
        prediction = model.predict([input_data])  # Adjust if your model expects a different format

        # Return the prediction in JSON format
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

