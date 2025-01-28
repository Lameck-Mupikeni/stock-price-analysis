import React, { useState } from 'react';

function StockForm({ onSubmit }) {
  const [symbol, setSymbol] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (symbol) {
      onSubmit(symbol);  // Call parent function to fetch data
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="symbol">Stock Symbol:</label>
      <input
        type="text"
        id="symbol"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter Stock Symbol (e.g., AAPL)"
      />
      <button type="submit">Fetch Data</button>
    </form>
  );
}

export default StockForm;
