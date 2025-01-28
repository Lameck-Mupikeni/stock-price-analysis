from flask import Flask, jsonify, request
from models.prediction_model import fetch_and_predict, make_prediction

app = Flask(__name__)

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', 'AAPL')
    result = fetch_and_predict(symbol)
    return jsonify(result)

@app.route('/api/predict', methods=['GET'])
def predict_stock():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Symbol parameter is required"}), 400  # Handle missing symbol
    
    predicted_prices = make_prediction(symbol)
    if predicted_prices is None:
        return jsonify({"error": "Could not fetch prediction data for the given symbol"}), 404
    
    return jsonify(predicted_prices)

if __name__ == "__main__":
    app.run(debug=True)
