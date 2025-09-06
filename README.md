# Weather Dashboard

A command-line Python application that fetches real-time weather data for any city using the OpenWeatherMap API. This project showcases API integration, JSON parsing, error handling, and basic user input handling—ideal for demonstrating data retrieval skills in a portfolio.

## Features
- Fetch current weather details: temperature, feels-like, description, humidity, and wind speed.
- Supports metric (Celsius) units by default; easily switchable to imperial.
- Interactive loop for multiple city queries.
- Error handling for invalid cities or API issues.

## Tech Stack
- Python 3.x
- Requests library for HTTP requests.

## Installation
1. Clone the repository: git clone https://github.com/yourusername/weather-dashboard.git
2. Navigate to the project directory: cd weather-dashboard
3. Install dependencies: pip install requests
4. 4. Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `"YOUR_API_KEY_HERE"` in `main.py`.

## Usage
1. Run the script: python main.py
2. 2. Enter a city name (e.g., "London") when prompted.
3. View the weather details.
4. Type "exit" to quit.
5. Example output: Weather in London:
Temperature: 15.2°C
Feels Like: 14.5°C
Description: Clear sky
Humidity: 70%
Wind Speed: 3.1 m/s

## Screenshots
- Command-Line Output: ![Weather Output Screenshot](screenshots/output.png) (Add a screenshot here).

## Future Improvements
- Add a graphical user interface (GUI) using Tkinter or Flask.
- Include 5-day forecast or weather maps.
- Support location-based queries via geolocation.
- Add unit conversion options in the CLI.

## Contributing
Contributions welcome! Open an issue or pull request for suggestions.

## License
MIT License - see [LICENSE](LICENSE) for details.
