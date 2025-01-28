from flask import Flask, jsonify, request
from flask_cors import CORS
from models.prediction_model import fetch_and_predict  
import pandas as pd  

app = Flask(__name__)
CORS(app)

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')  
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400
    
    try:
        prediction = fetch_and_predict(symbol)

        # Convert DataFrame to dictionary properly
        if isinstance(prediction, pd.DataFrame):
            prediction = prediction.to_dict(orient="index")

        # Convert keys (timestamps) to strings if needed
        if isinstance(prediction, dict):
            prediction = {str(key): value for key, value in prediction.items()} 

        return jsonify({"symbol": symbol, "prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
