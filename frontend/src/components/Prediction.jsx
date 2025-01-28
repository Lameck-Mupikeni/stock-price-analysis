// src/components/Prediction.jsx
import React from 'react';

const Prediction = ({ predictedData }) => {
  return (
    <div>
      <h2>Stock Price Prediction</h2>
      <ul>
        {predictedData.map((prediction, index) => (
          <li key={index}>Predicted Price: {prediction.price}</li>
        ))}
      </ul>
    </div>
  );
};

export default Prediction;
