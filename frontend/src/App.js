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
    setError(null);

    try {
      const response = await fetch(
        `https://stock-price-analysis-3.onrender.com/api/stock?symbol=${symbol}`
      );

      if (!response.ok) {
        throw new Error("Stock data not found");
      }

      const data = await response.json();
      console.log("API Response:", data);

      if (!data.prediction || typeof data.prediction !== "object") {
        throw new Error("Invalid response structure: 'prediction' is missing or incorrect");
      }

      // Transform API response into an object with date keys
      const formattedPredictions = {};
      Object.entries(data.prediction).forEach(([date, values]) => {
        formattedPredictions[date] = { mean: values.mean };
      });

      setStockData({
        symbol: data.symbol,
        predictions: formattedPredictions, // Store as an object
      });
    } catch (error) {
      console.error("Error fetching data:", error);
      setError(error.message);
    } finally {
      setLoading(false);
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
          stockData={stockData.predictions} // Pass stockData as an object
          stockSymbol={stockData.symbol} // Pass stock symbol
        />
      )}
    </div>
  );
}

export default App;
