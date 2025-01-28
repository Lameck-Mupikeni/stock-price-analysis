import React, { useState } from 'react';
import StockForm from './components/StockForm';
import StockChart from './components/StockChart';

function App() {
	  const [stockData, setStockData] = useState(null);

	  const fetchStockData = async (symbol) => {
		      const response = await fetch(`/api/stock?symbol=${symbol}`);
		      const data = await response.json();
		      setStockData(data);
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

