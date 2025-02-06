import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  
from models.prediction_model import fetch_and_predict  

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Ensure 'static' directory exists for storing generated plots
if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/api/stock', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')  
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        # Fetch and predict
        prediction = fetch_and_predict(symbol)

        print("Raw Prediction Output:", prediction)

        if isinstance(prediction, pd.DataFrame):
            prediction = prediction.to_dict(orient="index")

        print("Converted Prediction Output:", prediction)

        # Convert dictionary keys to strings
        prediction = {str(key): value for key, value in prediction.items()}

        # Generate and save stock price visualization
        dates = list(prediction.keys())
        means = [data["mean"] for data in prediction.values()]

        plt.figure(figsize=(10, 5))
        sns.lineplot(x=dates, y=means, marker="o", label=f"{symbol} Price Prediction")
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Predicted Price")
        plt.title(f"Stock Price Prediction for {symbol}")
        plt.legend()
        plt.grid()

        # Save the plot
        chart_filename = f"stock_chart_{symbol}.png"
        chart_path = os.path.join("static", chart_filename)
        plt.savefig(chart_path)
        plt.close()

        return jsonify({
            "symbol": symbol,
            "prediction": prediction,
            "chart_url": f"/static/{chart_filename}"  # URL to access chart
        })

    except Exception as e:
        print("Error during fetch_and_predict:", str(e))
        return jsonify({"error": str(e)}), 500

# Serve static files (for the chart image)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory("static", filename)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
