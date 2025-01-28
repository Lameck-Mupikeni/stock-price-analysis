import requests
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

def fetch_data(symbol):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }
    response = requests.get(url, params=params)
    data = response.json()
    time_series = data['Time Series (Daily)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    
    # Convert the datetime index to string format
    df.index = df.index.strftime('%Y-%m-%d')
    
    return df

def predict_stock_prices(df):
    df = df['4. close']  # Focus on closing prices
    df = df.sort_index()
    model = ARIMA(df, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)        
    return forecast.tolist()

def fetch_and_predict(symbol):
    df = fetch_data(symbol)
    predictions = predict_stock_prices(df)
    result = {
        'last_prices': df['4. close'].to_dict(),  # Convert to dictionary for easy JSON serialization
        'predictions': predictions
    }
    return result
