from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load your model (use pickle or TensorFlow depending on your model)
with open('fraud_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route to render index.html
@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html from templates folder

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')

    if features:
        # Convert the features into a format suitable for the model
        features_array = np.array(features).reshape(1, -1)
        # Make a prediction using the loaded model
        prediction = model.predict(features_array)

        # Return the prediction result
        result = "fraud" if prediction[0] == 1 else "not fraud"
        return jsonify({"prediction": result})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
