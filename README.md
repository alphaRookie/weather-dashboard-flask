# Weather Dashboard — Flask 

A lightweight weather app (dashboard-style) built with Flask that allows users to search for real-time weather information by city and country code. The application integrates with the OpenWeatherMap API and focuses on clean request handling, error management, and a smooth user experience.  The application is fully **dockerized** for easy setup and execution.

---

## Demo

![Weather App Screenshot](Screenshot.png)

---

## Key Features

- Search current weather by city and country code
- Real-time data fetched from OpenWeatherMap API
- Clear error handling for invalid input and API failures
- Prevents duplicate form submission on page refresh using Post/Redirect/Get (PRG)
- Environment-based configuration for sensitive data
- Responsive layout optimized for both desktop and mobile devices
- Dockerized for consistent execution across different environments

---

## Tech Stack

- Backend: Python, Flask
- Frontend: HTML, Jinja2, Bootstrap
- API: OpenWeatherMap
- Environment Management: python-dotenv
- Containerization: Docker

---

## How It Works

1. User submits city and country code via a form.
2. The app validates input and requests geolocation data from the API.
3. Coordinates are used to fetch current weather data.
4. Results or error messages are stored temporarily using Flask sessions.
5. The app redirects to a GET request to safely render the result.
6. Session data is cleared after display to prevent repeated output on refresh.

---

## Installation & Setup

Firstly, make sure Docker is installed and running

1. Clone the repository:
   ```bash
   git clone https://github.com/alphaRookie/weather-dashboard-flask.git
   ```

2. Move into project directory:
   ```bash
   cd weather-dashboard-flask
   ```

3. Build the Docker image:
   ```bash
   docker build -t myweatherapp .
   ```

4. Run the Docker container:
   ```bash
   docker run -p 5000:5000 -e API_KEY=YOUR_API_KEY myweatherapp
   ```
   ⚠️ Replace YOUR_API_KEY with your own OpenWeatherMap API key.

5. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000
   ```
