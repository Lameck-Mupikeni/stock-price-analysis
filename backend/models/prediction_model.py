from pmdarima import auto_arima

def fetch_and_predict(symbol, forecast_days=10):
    try:
        df = get_stock_data(symbol)
        df = format_date_column(df)
        df.set_index('Date', inplace=True)

        # Handle missing values
        df = df.fillna(method='ffill')

        # Stationarity check and differencing
        df['Close'] = df['Close'].diff().dropna()

        # Use auto_arima to automatically select the best model
        model = auto_arima(df['Close'], seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
        model.fit(df['Close'])
        forecast = model.predict(n_periods=forecast_days)

        # Convert forecast to DataFrame and handle timestamps
        forecast_dates = pd.date_range(start=df.index[-1], periods=forecast_days + 1, freq='D')[1:]
        forecast_df = pd.DataFrame(forecast, index=forecast_dates, columns=['Prediction'])
        forecast_df = format_date_column(forecast_df)

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
