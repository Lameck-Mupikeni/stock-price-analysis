from flask import Flask, jsonify, request
from flask_cors import CORS
from models.prediction_model import fetch_and_predict  # Adjust based on your structure
import pandas as pd  # Ensure pandas is imported

app = Flask(__name__)
CORS(app)

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')  # Get symbol from query parameters
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400
    
    try:
        prediction = fetch_and_predict(symbol)

        # If the result is a DataFrame, convert Timestamps to strings
        if isinstance(prediction, pd.DataFrame):
            prediction = prediction.applymap(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)
            prediction = prediction.to_dict(orient="records")
        
        # If the result is already a dictionary or list of dictionaries, convert Timestamps
        elif isinstance(prediction, list):
            prediction = [
                {key: (value.isoformat() if isinstance(value, pd.Timestamp) else value) for key, value in record.items()}
                for record in prediction
            ]
        elif isinstance(prediction, dict):
            prediction = {key: (value.isoformat() if isinstance(value, pd.Timestamp) else value) for key, value in prediction.items()}

        return jsonify({"symbol": symbol, "prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
