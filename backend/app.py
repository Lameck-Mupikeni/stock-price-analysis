from flask import Flask, request, jsonify
from models.prediction_model import fetch_and_predict  # Adjust the import to match your file structure
import pandas as pd  # Ensure this is imported for DataFrame operations

# Initialize the Flask app
app = Flask(__name__)

# Define the route
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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
