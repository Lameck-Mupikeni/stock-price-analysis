import React, { useState } from 'react';

function StockForm({ onSubmit }) {
  const [symbol, setSymbol] = useState('');
  const [error, setError] = useState('');  // To manage error state

  const handleSubmit = (e) => {
    e.preventDefault();

    if (symbol) {
      setError('');  // Reset any previous errors
      onSubmit(symbol);  // Call parent function to fetch data
    } else {
      setError('Please enter a valid stock symbol.');  // Show error message if symbol is empty
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

      {error && <p style={{ color: 'red' }}>{error}</p>}  {/* Display error message if any */}
    </form>
  );
}

export default StockForm;
