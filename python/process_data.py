import pandas as pd

def parse_weather(entry):
    if entry is None:
        return None
    return {
        'Datetime': pd.to_datetime(entry['dt'], unit='s'),
        'Temperature (C)': entry['main']['temp'] - 273.15,
        'Humidity (%)': entry['main']['humidity'],
        'Wind Speed (m/s)': entry['wind']['speed'],
        'Weather': entry['weather'][0]['description']
    }

def save_to_csv(data, filename):
    if data is None:
        print(f"No data to save for {filename}")
        return
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    #print(f"{filename} saved")

def calculate_daily_stats(forecast_data):
    if forecast_data is None:
        return None
    
    df_forecast = pd.DataFrame(forecast_data)
    df_forecast['Date'] = df_forecast['Datetime'].dt.date

    daily_stats = df_forecast.groupby('Date').agg({
        'Temperature (C)': ['min', 'max'],
        'Humidity (%)': ['min', 'max'],
        'Wind Speed (m/s)': ['min', 'max']
    })

    daily_stats.columns = ['Min Temperature (C)', 'Max Temperature (C)', 
                           'Min Humidity (%)', 'Max Humidity (%)', 
                           'Min Wind Speed (m/s)', 'Max Wind Speed (m/s)']
    
    daily_stats.reset_index(inplace=True)
    
    return daily_stats

def process_weather_data(current_data, forecast_data):
    current_weather = parse_weather(current_data)
    forecast_weather = [parse_weather(entry) for entry in forecast_data['list']]
    
    save_to_csv([current_weather], 'current_weather_data.csv')
    save_to_csv(forecast_weather, 'hourly_weather_data.csv')
    
    daily_stats = calculate_daily_stats(forecast_weather)
    save_to_csv(daily_stats, 'daily_weather_stats.csv')
    
    return pd.DataFrame([current_weather]), pd.DataFrame(forecast_weather), daily_stats
