@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')  
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400
    
    try:
        prediction = fetch_and_predict(symbol)

        # Ensure proper JSON serialization
        if isinstance(prediction, pd.DataFrame):
            prediction = prediction.to_dict(orient="index")
        
        # Convert any non-string keys to strings
        prediction = {str(key): value for key, value in prediction.items()}

        return jsonify({"symbol": symbol, "prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
