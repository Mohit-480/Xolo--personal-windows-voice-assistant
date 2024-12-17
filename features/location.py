import requests

def get_location():
    try:
        url = "https://freegeoip.app/json/"
        response = requests.get(url)
        data = response.json()
        city = data.get("city", "unknown location")
        return city
    except Exception as e:
        print(f"Error fetching location: {e}")
        return "unknown location"
