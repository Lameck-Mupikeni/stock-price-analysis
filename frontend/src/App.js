import React, { useState } from 'react';
import StockForm from './components/StockForm';
import StockChart from './components/StockChart';

function App() {
  const [stockData, setStockData] = useState(null);

  const fetchStockData = async (symbol) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/stock?symbol=${symbol}`);
      
      // Check if the response is successful
      if (!response.ok) {
        throw new Error('Stock data not found');
      }

      const data = await response.json();
      console.log(data);  // Check the structure of the data in the console

      // Update the state with the fetched data
      setStockData(data);
    } catch (error) {
      console.error('Error fetching data:', error);  // Log the error in the console for debugging
      alert('Error fetching data: ' + error.message);  // Display the error message to the user
    }
  };

  return (
    <div>
      <h1>Stock Price Analysis</h1>
      {/* Pass the fetchStockData function as a prop to the StockForm */}
      <StockForm onSubmit={fetchStockData} />

      {stockData && (
        <StockChart
          data={{
            dates: Object.keys(stockData.prediction),  // Get the dates from the prediction object
            prices: Object.values(stockData.prediction).map(item => item.mean),  // Use the 'mean' value from the prediction
          }}
          predictions={stockData.prediction}  // Pass the entire prediction data to StockChart
        />
      )}
    </div>
  );
}

export default App;
