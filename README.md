## Github Repository link: 
https://lameck-mupikeni.github.io/stock-price-analysis/
## Deplyed Application link: 
https://github.com/Lameck-Mupikeni/stock-price-analysis

## Stock Price Analysis and Prediction
This project is a stock price analysis and prediction web application that allows users to input stock symbols and get predicted future stock prices. The application uses Flask as the backend for API services and React for the frontend, integrating machine learning models for stock price predictions.

## Project Overview
The backend of the application is a Flask API that uses a machine learning model to predict future stock prices based on historical data. The frontend, built with React, allows users to input stock symbols and view interactive charts displaying the predictions.

## Key Features:
Stock Symbol Input: Users can input a stock symbol to retrieve data.
Prediction Data: The backend fetches historical data and uses a predictive model to forecast future stock prices.
Interactive Charts: The frontend displays the predictions in interactive charts using the data retrieved from the backend.
Cross-Origin Resource Sharing (CORS): The backend has CORS enabled to allow the frontend to communicate seamlessly with the Flask API.
Repository Information
Frontend Repository: Stock Price Analysis Frontend
Backend Repository: Stock Price Analysis Backend
Backend

## The backend is developed using Flask and includes the following:

API Endpoints: A /api/stock endpoint accepts a symbol query parameter, processes the data, and returns predictions.
Machine Learning Model: The prediction model fetches data, processes it, and returns predictions for stock prices.
Setup Instructions for Backend:
Clone the repository.
Navigate to the backend directory.
Install the required dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run the application:
bash
Copy
Edit
python app.py
The application will be available on http://localhost:5000.

## Frontend
The frontend is developed using React and includes:

StockForm: A form where users can input a stock symbol.
StockChart: A chart displaying the predicted stock prices.
Setup Instructions for Frontend:
Navigate to the frontend directory.
Install the required dependencies:
bash
Copy
Edit
npm install
Start the React development server:
bash
Copy
Edit
npm start
The frontend will be available on http://localhost:3000.
Deployment
The project is deployed using GitHub Pages.

## Backend Deployment:
Ensure the Flask app is correctly set up with the required environment variables.
Link the backend repository to your hosting service (e.g., Render or any cloud service).
Set up the environment variables:
PORT: Default is 1000 (or your service will assign one dynamically).
Deploy the backend.
Frontend Deployment:
Link the frontend repository to GitHub Pages or your preferred hosting service.
Deploy the frontend.
Once both parts are deployed, the app will be accessible at https://lameck-mupikeni.github.io/stock-price-analysis/.

## API Documentation
Endpoint: /api/stock
Method: GET
Query Parameters:
symbol: The stock symbol (e.g., AAPL).
Response:
A JSON response containing the stock symbol and the predicted future prices.

json
Copy
Edit
{
  "symbol": "AAPL",
  "prediction": {
    "2025-01-31": { "mean": 150.25 },
    "2025-02-01": { "mean": 152.50 },
    "2025-02-02": { "mean": 154.75 }
  }
}
## Troubleshooting
If the application is not working correctly, consider the following troubleshooting steps:

Backend API not responding: Ensure that the Flask app is running and accessible on the correct port.
CORS issues: If you're seeing errors related to cross-origin requests, ensure that Flask-CORS is installed and configured properly.
Invalid data: Ensure that the correct stock symbol is entered in the frontend form.

## Technologies Used
Backend: Flask, Flask-CORS
Frontend: React, Chart.js
Machine Learning: Custom predictive model
Hosting: GitHub Pages, Render

## License
This project is licensed under the MIT License - see the LICENSE file for details.

