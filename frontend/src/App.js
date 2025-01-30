import React, { useState } from 'react';
import StockForm from './components/StockForm';
import StockChart from './components/StockChart';
import './styles.css';  // Import the stylesheet

function App() {
  const [stockData, setStockData] = useState(null);

  const fetchStockData = async (symbol) => {
    try {
      // Use the deployed URL for the API
      const response = await fetch(`https://stock-price-analysis-2.onrender.com/api/stock?symbol=${symbol}`);
      
      if (!response.ok) {
        throw new Error('Stock data not found');
      }

      const data = await response.json();
      console.log("API Response:", data); // Debugging: Log the API response structure

      if (!data.prediction || typeof data.prediction !== "object") {
        throw new Error("Invalid response structure: 'prediction' is missing or incorrect");
      }

      // Ensure `data.prediction` is in the correct format
      const formattedPredictions = Object.entries(data.prediction).map(([date, values]) => ({
        date,
        mean: values.mean,
      }));

      setStockData({
        symbol: data.symbol,
        predictions: formattedPredictions,
      });

    } catch (error) {
      console.error('Error fetching data:', error);
      alert('Error fetching data: ' + error.message);
    }
  };

  return (
    <div>
      <h1>Stock Price Analysis</h1>
      <StockForm onSubmit={fetchStockData} />

      {stockData && (
        <StockChart
          data={{
            dates: stockData.predictions.map(item => item.date),  // Extract dates
            prices: stockData.predictions.map(item => item.mean),  // Extract predicted prices
          }}
          predictions={stockData.predictions}  // Pass formatted predictions to StockChart
        />
      )}
    </div>
  );
}

export default App;
