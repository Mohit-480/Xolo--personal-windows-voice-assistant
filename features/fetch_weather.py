from bs4 import BeautifulSoup
import requests
from head.mouth import speak  # Replace with your own text-to-speech module


def fetch_weather(city):
    """Fetch and speak the weather using Google search."""
    try:
        # Construct the Google search URL for the weather
        url = f"https://www.google.com/search?q=weather+in+{city}"
        headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a browser to avoid blocking
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape the relevant data from Google's weather widget
        region = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
        temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
        day = soup.find_all("div", class_="BNeawe tAd8D AP7Wnd")

        # Ensure all data is available
        if not region or not temp or len(day) < 2:
            speak("Sorry, I couldn't fetch the weather data. Please try again later.")
            return

        # Extract text from the elements
        weather = day[1].text if len(day) > 1 else "unknown weather"
        temperature = temp.text.split("°")[0] if temp else "unknown temperature"

        # Speak the weather information
        speak(f"It's currently {weather} and {temperature} degrees Celsius in {region.text}.")
        print(f"It's currently {weather} and {temperature} degrees Celsius in {region.text}.")

    except Exception as e:
        speak("An error occurred while fetching the weather. Please try again later.")
        print(f"Error in fetch_weather: {e}")
