import React, { useState } from 'react';

const StockForm = ({ onSubmit }) => {
	  const [symbol, setSymbol] = useState('AAPL');

	  const handleSubmit = (e) => {
		      e.preventDefault();
		      onSubmit(symbol);
		    };

	  return (
		      <form onSubmit={handleSubmit}>
		        <label htmlFor="symbol">Stock Symbol:</label>
		        <input
		          type="text"
		          id="symbol"
		          value={symbol}
		          onChange={(e) => setSymbol(e.target.value)}
		        />
		        <button type="submit">Fetch Data</button>
		      </form>
		    );
};

export default StockForm;

