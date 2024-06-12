def determine_weather(row, sunny_threshold, rainy_min_temp_threshold, rainy_humidity_threshold):
    """
    Determine the weather condition based on temperature and humidity thresholds.

    Args:
        row (dict): A dictionary representing a single day's weather data with keys 'Max Temperature (C)', 
                    'Min Temperature (C)', and 'Max Humidity (%)'.
        sunny_threshold (float): The temperature threshold above which the weather is considered 'Sunny'.
        rainy_min_temp_threshold (float): The minimum temperature threshold below which, combined with high humidity, 
                                          the weather is considered 'Rainy'.
        rainy_humidity_threshold (float): The humidity threshold above which, combined with low temperature, 
                                          the weather is considered 'Rainy'.

    Returns:
        str: A string indicating the weather condition, which can be 'Sunny', 'Rainy', or 'Partly Cloudy'.
    """
    if row['Max Temperature (C)'] > sunny_threshold:
        return 'Sunny'
    elif row['Min Temperature (C)'] < rainy_min_temp_threshold and row['Max Humidity (%)'] > rainy_humidity_threshold:
        return 'Rainy'
    else:
        return 'Partly Cloudy'


def convert_temperature(kelvin):
    """
    Convert temperature from Kelvin to Celsius.

    Args:
        kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = kelvin - 273.15
    return celsius
