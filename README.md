# Telegram Weather Bot Deployment Report

## 1. Introduction

This report documents the design, development, and deployment of a simple Telegram bot that provides real-time weather information for Saudi Arabian cities. The project was implemented in Python using the `python-telegram-bot` library and deployed on Heroku using its Platform as a Service (PaaS) capabilities.

## 2. Bot Functionality

The bot interacts with users through Telegram and provides weather updates based on the city selected. It supports the following features:
* Interactive reply keyboard with a list of major Saudi cities.
* Real-time weather data fetched from the OpenWeatherMap API.
* Arabic language support for user communication and weather descriptions.

## 3. Technologies Used

* **Programming Language:** Python
* **Bot Library:** `python-telegram-bot`
* **API Service:** OpenWeatherMap
* **Deployment Platform:** Heroku
* **Version Control:** Git
* **Other Tools:** `requests`, `os`, Heroku CLI

## 4. Project Structure

The project included the following core files:
* `main.py`: The main script containing bot logic. 
* `requirements.txt`: A list of dependencies for Heroku.
* `Procfile`: Used by Heroku to know how to run the app.

**Example `Procfile` content:**
**Example `requirements.txt`:**
ذ
## 5. Deployment Steps


1.  **Create Telegram Bot**
    * Used BotFather to create a bot and obtain the BOT_TOKEN.

2.  **Set Up Heroku App**
    * Created a new Heroku app via Heroku CLI or dashboard.
    * Added environment variables (config vars):
        ```bash
        heroku config:set BOT_TOKEN=your_token --app your-app-name
        heroku config:set WEATHER_API_KEY=your_openweather_api_key --app your-app-name
        ```
       
3.  **Deploy via Git**
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    heroku git:remote -a your-app-name
    git push heroku main
    ```
   
4.  **Scale Dyno**
    ```bash
    heroku ps:scale worker=1
    ```
   
5.  **Monitor Logs**
    ```bash
    heroku logs --tail
    ```
   

## 6. Bot Test & Output

The bot was tested successfully via the Telegram app. When a user starts the bot, it presents a keyboard with a list of Saudi cities. Upon selecting a city, the bot fetches and responds with live weather data in Arabic.

**Example reply:**
> "الطقس في الرياض:
> درجة الحرارة: 38°C
> الحالة: مشمس"

## 7. Conclusion

This project successfully demonstrates how to build, deploy, and operate a Telegram bot using Python and Heroku. It leverages APIs and cloud services to deliver real-time data, offering an engaging user experience with minimal infrastructure overhead.

## 8. Screenshot

![Bot Screenshot](bot-screenshot.jpg)

