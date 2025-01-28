import React, { useState } from 'react';
import StockForm from './components/StockForm';
import StockChart from './components/StockChart';
import './styles.css';  // Import the stylesheet

function App() {
  const [stockData, setStockData] = useState(null);

  const fetchStockData = async (symbol) => {
    const response = await fetch(`/api/stock?symbol=${symbol}`);
    const data = await response.json();
    setStockData(data);
  };

  return (
    <div className="container">
      <h1>Stock Price Analysis</h1>
      <StockForm onSubmit={fetchStockData} />
      {stockData && (
        <div className="chart-container">
          <h2>Stock Price Chart</h2>
          <StockChart
            data={{
              dates: Object.keys(stockData.last_prices),
              prices: Object.values(stockData.last_prices),
            }}
            predictions={stockData.predictions}
          />
        </div>
      )}
    </div>
  );
}

export default App;
