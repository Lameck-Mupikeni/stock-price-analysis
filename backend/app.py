from flask import Flask, jsonify, request
from models.prediction_model import fetch_and_predict

app = Flask(__name__)

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', 'AAPL')  # Default to 'AAPL' if no symbol provided
    result = fetch_and_predict(symbol)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
