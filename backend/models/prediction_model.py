import pandas as pd
from models.stock_data import get_stock_data  # Ensure this function fetches stock data correctly

def fetch_and_predict(symbol, days=10):
    try:
        # Fetch historical stock data
        df = get_stock_data(symbol)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df = df.asfreq('D')  # Ensure daily frequency

        # Placeholder forecasting model (replace with an actual model)
        model = some_model.fit(df['Close'])  # Assuming 'Close' is the column to forecast
        forecast = model.get_forecast(steps=days)
        forecast_df = forecast.summary_frame()
        forecast_df.index = forecast_df.index.strftime('%Y-%m-%d')  # Format index as date strings

        # Merge historical data with predictions
        historical_prices = df['Close'].tail(10).to_dict()
        return {
            "symbol": symbol,
            "historical_prices": historical_prices,
            "prediction": forecast_df.to_dict(orient="index")
        }
    except Exception as e:
        return {"error": str(e)}
