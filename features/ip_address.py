from head.mouth import speak
import requests
def get_ip_address():
    """Get the public IP address of the user."""
    ip = requests.get('https://api.ipify.org').text
    speak(f"Your IP address is {ip}")
    print(f"Your IP address is {ip}")
    return ip