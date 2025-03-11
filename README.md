# Weather Forecast Project

A Python-based weather forecast project that uses the Tomorrow.io API to retrieve weather data.

![![alt text](get real time weather usage)](docs/media/real_time_weather_usage.gif)

![![alt text](project scheme)](<docs/media/project scheme.png>)

## Getting Started

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/zana-abdi2002/get-weather.git`
2. Create a new file named `.env` in the root of the repository.
3. Add the following line to the `.env` file: `API_KEY=YOUR_API_KEY_HERE`
4. Replace `YOUR_API_KEY_HERE` with your actual Tomorrow.io API key.
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the project: `python main.py`

## Usage

Important Note for Users in Iran

Due to internet restrictions in Iran, users may need to use a VPN to access the Tomorrow.io API and use this project.

The project provides the following commands:

- `get`: Retrieves the current weather for a specified city.
- `get -t`: Retrieves the today's weather forecast for a specified city.
- `get -x`: Retrieves the tomorrow's weather forecast for a specified city.

Example usage:

```shell
$ python main.py get sanandaj -n
returned cache

sanandaj now:
+---------------------------+----------+
| Weather Condition         | Value    |
+===========================+==========+
| Temperature               | -2.1°C   |
+---------------------------+----------+
| Feels Like                | -2.1°C   |
+---------------------------+----------+
| Humidity                  | 78%      |
+---------------------------+----------+
| Wind Speed                | 0.5 m/s  |
+---------------------------+----------+
| Wind Direction            | 349°     |
+---------------------------+----------+
| Cloud Cover               | 35%      |
+---------------------------+----------+
| Precipitation Probability | 0%       |
+---------------------------+----------+
| Visibility                | 15.82 km |
+---------------------------+----------+

$ python main.py get -x shiraz
not in cache
added cache

shiraz tomorrow:
+---------------------------+-------------+
| Weather Condition         | Value       |
+===========================+=============+
| Temperature               | 10.3 | -2°C |
+---------------------------+-------------+
| Feels Like                | 3.3°C       |
+---------------------------+-------------+
| Humidity                  | 39%         |
+---------------------------+-------------+
| Wind Speed                | 2.7 m/s     |
+---------------------------+-------------+
| Wind Direction            | 275°        |
+---------------------------+-------------+
| Cloud Cover               | 0%          |
+---------------------------+-------------+
| Precipitation Probability | 0%          |
+---------------------------+-------------+
| Visibility                | 16 km       |
+---------------------------+-------------+
```

## Project Structure

The project is organized into the following directories:

**components**: Contains the Tomorrow.io API client and weather data processing logic.

**cache.py**: Handles caching of weather data.

**forcast_weather.py**: Retrieves weather forecast data from the Tomorrow.io API.

**real_time_weather.py**: Retrieves real-time weather data from the Tomorrow.io API.

**table.py**: Prints weather data in a tabular format.

**main.py**: Contains the main application logic and command-line interface. and the entry point of the application

## Dependencies

The project depends on the following libraries:

**requests**: For making HTTP requests to the Tomorrow.io API.

**python-dotenv**: For loading environment variables from the .env file.

**tabulate**: For printing weather data in a tabular format.

**argparse**: For parsing command-line arguments.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
