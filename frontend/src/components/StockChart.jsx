import React from 'react';
import { Line } from 'react-chartjs-2';

const StockChart = ({ data, predictions }) => {
  const chartData = {
    labels: data.dates,
    datasets: [
      {
        label: 'Historical Prices',
        data: data.prices,
        borderColor: 'blue',
        fill: false,
      },
      {
        label: 'Predicted Prices',
        data: predictions,
        borderColor: 'red',
        borderDash: [5, 5],
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default StockChart;
