import React, { useState } from 'react';
import StockForm from './components/StockForm';
import StockChart from './components/StockChart';
import './styles.css';  // Import the stylesheet

function App() {
  const [stockData, setStockData] = useState(null);

  const fetchStockData = async (symbol) => {
    try {
      const response = await fetch(`/api/stock?symbol=${symbol}`);
      if (!response.ok) {
        throw new Error('Stock data not found');
      }
      const data = await response.json();
      console.log(data);  // Verify the data is being fetched correctly
      setStockData(data); // Update stock data state
    } catch (error) {
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
            dates: Object.keys(stockData.last_prices),
            prices: Object.values(stockData.last_prices),
          }}
          predictions={stockData.predictions}
        />
      )}
    </div>
  );
}

export default App;
