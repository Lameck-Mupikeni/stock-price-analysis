import React from 'react';

function StockChart({ data, predictions }) {
  if (!data || !predictions) {
    return <p>No stock data available. Please fetch data first.</p>;
  }

  return (
    <div>
      <h2>Stock Data</h2>
      <table border="1" cellPadding="5" style={{ borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Date</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {data.dates.map((date, index) => (
            <tr key={date}>
              <td>{date}</td>
              <td>${data.prices[index].toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3>Predictions for the next 7 days</h3>
      {predictions.length > 0 ? (
        <ul>
          {predictions.map((prediction, index) => (
            <li key={index}>
              <strong>Day {index + 1} ({prediction.date}):</strong> ${prediction.mean.toFixed(2)}
            </li>
          ))}
        </ul>
      ) : (
        <p>No predictions available.</p>
      )}
    </div>
  );
}

export default StockChart;
