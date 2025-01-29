import pandas as pd
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

def get_stock_data(symbol):
    """Fetch historical stock data using Yahoo Finance"""
    try:
        stock = yf.download(symbol, period="1y")  # Fetch 1 year of data
        stock.reset_index(inplace=True)  # Ensure 'Date' is a column
        return stock
    except Exception as e:
        raise RuntimeError(f"Error fetching stock data: {e}")

def fetch_and_predict(symbol):
    # Fetch data (example)
    df = get_stock_data(symbol)  # Assuming this fetches a DataFrame with a 'Date' column
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is in datetime format
    df.set_index('Date', inplace=True)
    
    # Add a frequency to the date index
    df = df.asfreq('D')  # Adjust frequency to daily ('D') or as needed
    
    # Forecasting logic (example)
    model = ARIMA(df['Close'], order=(5,1,0))  # Adjust parameters if needed
    fitted_model = model.fit()
    forecast = fitted_model.get_forecast(steps=10)
    
    # Convert forecast to DataFrame and handle timestamps
    forecast_df = forecast.summary_frame()
    forecast_df.index = forecast_df.index.to_pydatetime()  # Ensure index is datetime

    return forecast_df
