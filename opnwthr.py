import streamlit as st
import requests

# ----------------------------
# Weather App
# ----------------------------

st.title("🌤 Weather App")

# User input
city = st.text_input("Enter City Name")

# Your Weather API Key
API_KEY = "WEATHER_API_KEY"

# Button
if st.button("Get Weather"):

    if city == "":
        st.warning("Please enter a city name.")

    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]

            st.success("Weather Information")

            st.write(f"🌍 City: {city}")
            st.write(f"🌡 Temperature: {temperature} °C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁ Condition: {weather}")

        else:
            st.error("City not found.")