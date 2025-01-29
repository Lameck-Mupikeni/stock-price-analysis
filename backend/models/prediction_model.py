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
        raise ValueError(f"Error fetching stock data for symbol {symbol}: {e}")

def format_date_column(df):
    """Convert the Date column to a more readable format"""
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
    return df

def fetch_and_predict(symbol, forecast_days=10):
    """Fetch stock data and make predictions"""
    try:
        df = get_stock_data(symbol)  # Fetch the stock data
        df = format_date_column(df)  # Convert Date to readable format
        df.set_index('Date', inplace=True)
        
        # Add a frequency to the date index
        df = df.asfreq('D')  # Adjust frequency to daily ('D') or as needed
        
        # Forecasting logic
        model = ARIMA(df['Close'], order=(5,1,0))  # Adjust parameters if needed
        fitted_model = model.fit()
        forecast = fitted_model.get_forecast(steps=forecast_days)
        
        # Convert forecast to DataFrame and handle timestamps
        forecast_df = forecast.summary_frame()
        forecast_df.index = forecast_df.index.to_pydatetime()  # Ensure index is datetime
        forecast_df = format_date_column(forecast_df)  # Convert forecast dates to readable format
        
        # Include past stock prices
        past_prices = df.reset_index().to_dict(orient='records')
        predictions = forecast_df.reset_index().to_dict(orient='records')
        
        # Return nested response with historical prices and predictions
        response = {
            'symbol': symbol,
            'historical_prices': past_prices,
            'predictions': predictions
        }
        
        return response
        
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {e}"}
