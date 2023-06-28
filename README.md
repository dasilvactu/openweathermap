# opemweathermap API

This project aims to demonstrate the integration of different APIs, such as the Twitter API for managing tweets and the OpenWeather API for retrieving weather data.
Taking advantage of these APIs, the user can publish a tweet with the current weather of a city and the average temperature forecast for 5 days

Example of a tweet:

   23.6°C e nuvens dispersas em Muriae,BR em 27/06. Média para os próximos dias: 21.9°C em 28/06, 21.1°C em 29/06, 19.2°C em 30/06, 19.2°C em 01/07 e 17.9°C em 02/07.
# Prerequisites
Before running the API, make sure you have the following credentials available:

- Twitter API Credentials (https://developer.twitter.com/): 

    - Consumer Key: `<twitter_consumer_key>`
    - Consumer Secret: `<twitter_consumer_secret>`
    - Access Token: `<twitter_access_token>`
    - Access Token Secret: `<twitter_access_token_secret>`
- OpenWeather API Key (https://openweathermap.org/): `<open_weather_api_key>`

# Installation 

Follow the steps below to set up and run the openweather API:

1. Make sure you have [Docker](https://www.docker.com/) and [Docker-compose](https://docs.docker.com/compose/) installed on your system.
2. Clone this repository to your local environment.
3. Create a new file named .env in the root directory.
4. Open the .env file in a text editor and add the following lines:
   ```
   TWITTER_CONSUMER_KEY=<twitter_consumer_key>
   TWITTER_CONSUMER_SECRET=<twitter_consumer_secret>
   TWITTER_ACCESS_TOKEN=<twitter_access_token>
   TWITTER_ACCESS_TOKEN_SECRET=<twitter_access_token_secret>
   OPEN_WEATHER_API_KEY=<open_weather_api_key>
   ```
5. Build and start the Docker containers using Docker Compose.

` docker-compose up -d `

The API is now running locally at http://localhost:5000/.


# Endpoints

The API has the following endpoints:

- POST /publish_weather/<city> : This endpoint allows publishing weather information in twitter for a specific city using the POST method. City must be in pattern `<city>,<countryCode>`

Example

```
POST /publish_weather/ HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "city": "Rio de Janeiro, BR"
}
```

return 200

``` Weather and forecast publish successfully ```

- POST /publish_weather_sdk/<city> : This endpoint allows publishing weather information in twitter for a specific city using the POST method, using the sdk openweathermapsdk. City must be in pattern `<city>,<countryCode>`. 

Example

```
POST /publish_weather_sdk/ HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
  "city": "Rio de Janeiro, BR"
}
```

return 200

``` Weather and forecast publish successfully ```

# Testing
To run the unit tests, follow the steps below:
1. Make sure the container are up
2. All tests are in `tests` folder. You can run an especific test with the command:

` docker exec <container_name> python -m unittest tests/test_<name>.py `

To know container name, tou can run:
` docker ps `
and get the container name

