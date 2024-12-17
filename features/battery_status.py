import psutil

def battery_status():
    """Check the battery status and return its percentage and charging state."""
    try:
        battery = psutil.sensors_battery()
        if battery:
            status = f"Battery is at {battery.percent}%, and it is {'plugged in' if battery.power_plugged else 'not plugged in'}."
            print(status)
            return status
        else:
            print("Battery status could not be retrieved.")
            return "Battery status could not be retrieved."
    except Exception as e:
        print(f"Error fetching battery status: {e}")
        return "Error fetching battery status."
