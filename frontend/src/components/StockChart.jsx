import React from 'react';

function StockChart({ data, predictions }) {
  return (
    <div>
      <h2>Stock Data</h2>
      <table>
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
              <td>{data.prices[index]}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3>Predictions for the next 7 days</h3>
      <ul>
        {predictions && predictions.map((prediction, index) => (
          <li key={index}>Day {index + 1}: {prediction}</li>
        ))}
      </ul>
    </div>
  );
}

export default StockChart;
