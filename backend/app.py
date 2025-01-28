from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from models.prediction_model import fetch_and_predict

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', 'AAPL')
    result = fetch_and_predict(symbol)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
