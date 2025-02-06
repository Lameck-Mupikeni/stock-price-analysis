import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const StockChart = ({ stockData, stockSymbol }) => {
  if (!stockData) return <p>Loading chart...</p>;

  const labels = Object.keys(stockData);
  const values = Object.values(stockData).map(data => data.mean);

  const data = {
    labels,
    datasets: [
      {
        label: `Stock Price Prediction for ${stockSymbol}`,
        data: values,
        borderColor: "rgb(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderWidth: 2,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: true },
      tooltip: { enabled: true },
    },
  };

  return <Line data={data} options={options} />;
};

export default StockChart;
