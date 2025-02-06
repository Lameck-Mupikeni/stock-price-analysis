import React, { useState } from "react";
import StockForm from "./components/StockForm";
import StockChart from "./components/StockChart";
import "./styles.css"; // Import the stylesheet

function App() {
  const [stockData, setStockData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchStockData = async (symbol) => {
    setLoading(true);
    setError(null); // Reset error message before making a request

    try {
      // Fetch stock data from the deployed backend API
      const response = await fetch(
        `https://stock-price-analysis-3.onrender.com/api/stock?symbol=${symbol}`
      );

      if (!response.ok) {
        throw new Error("Stock data not found");
      }

      const data = await response.json();
      console.log("API Response:", data); // Debugging: Log API response

      if (!data.prediction || typeof data.prediction !== "object") {
        throw new Error(
          "Invalid response structure: 'prediction' is missing or incorrect"
        );
      }

      // Convert API response into a usable format for Chart.js
      const formattedPredictions = Object.entries(data.prediction).map(
        ([date, values]) => ({
          date,
          mean: values.mean,
        })
      );

      setStockData({
        symbol: data.symbol,
        predictions: formattedPredictions,
      });
    } catch (error) {
      console.error("Error fetching data:", error);
      setError(error.message); // Store error message for UI display
    } finally {
      setLoading(false); // Stop loading
    }
  };

  return (
    <div className="app-container">
      <h1>Stock Price Analysis</h1>
      <StockForm onSubmit={fetchStockData} />

      {loading && <p>Fetching data...</p>}
      {error && <p className="error-message">Error: {error}</p>}

      {stockData && (
        <StockChart
          data={{
            dates: stockData.predictions.map((item) => item.date), // Extract dates
            prices: stockData.predictions.map((item) => item.mean), // Extract predicted prices
          }}
          predictions={stockData.predictions} // Pass formatted predictions to StockChart
          stockSymbol={stockData.symbol} // Pass stock symbol for better display
        />
      )}
    </div>
  );
}

export default App;
