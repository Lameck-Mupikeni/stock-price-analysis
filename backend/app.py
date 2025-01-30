import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import flask_cors
from models.prediction_model import fetch_and_predict  # Adjust the import to match your file structure
import pandas as pd  # Ensure this is imported for DataFrame operations

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the stock prediction route
@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')  
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        # Fetch and predict
        prediction = fetch_and_predict(symbol)

        # Debugging: Log the prediction result
        print("Raw Prediction Output:", prediction)

        # Ensure proper JSON serialization
        if isinstance(prediction, pd.DataFrame):
            prediction = prediction.to_dict(orient="index")

        # Debugging: Log the dictionary-converted output
        print("Converted Prediction Output:", prediction)

        # Convert any non-string keys to strings
        prediction = {str(key): value for key, value in prediction.items()}

        return jsonify({"symbol": symbol, "prediction": prediction})

    except Exception as e:
        # Debugging: Log the exception
        print("Error during fetch_and_predict:", str(e))
        return jsonify({"error": str(e)}), 500

# Define the home route
@app.route('/')
def home():
    return "Hello, World!"

# Run the Flask app with the appropriate host and port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1000))  # Default to 1000 if PORT isn't set
    app.run(host="0.0.0.0", port=port)
