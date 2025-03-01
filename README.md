# Weather Forecast Project

A Python-based weather forecast project that uses the Tomorrow.io API to retrieve weather data.

## Getting Started

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/weather-forecast.git`
2. Create a new file named `.env` in the root of the repository.
3. Add the following line to the `.env` file: `API_KEY=YOUR_API_KEY_HERE`
4. Replace `YOUR_API_KEY_HERE` with your actual Tomorrow.io API key.
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the project: `python main.py`

## Usage

The project provides the following commands:

- `get`: Retrieves the current weather for a specified city.
- `get -t`: Retrieves the today's weather forecast for a specified city.
- `get -x`: Retrieves the tomorrow's weather forecast for a specified city.

Example usage:

```shell
$ python main.py get New York
Current weather in New York:
  Temperature: 22°C
  Feels like: 20°C
  Humidity: 60%
  Wind speed: 10 km/h
  Wind direction: NW
  Cloud cover: 20%
  Precipitation probability: 0%
  Visibility: 10 km

$ python main.py get -t New York
Today's weather forecast in New York:
  Temperature: 25°C
  Feels like: 23°C
  Humidity: 50%
  Wind speed: 15 km/h
  Wind direction: NW
  Cloud cover: 30%
  Precipitation probability: 10%
  Visibility: 15 km

$ python main.py get -x New York
Tomorrow's weather forecast in New York:
  Temperature: 28°C
  Feels like: 26°C
  Humidity: 40%
  Wind speed: 20 km/h
  Wind direction: NW
  Cloud cover: 40%
  Precipitation probability: 20%
  Visibility: 20 kmk
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
