import screen_brightness_control as sbc

def increase_brightness():
    """Increase screen brightness by 10%, up to a maximum of 100%."""
    try:
        current_brightness = sbc.get_brightness()
        if isinstance(current_brightness, list):
            current_brightness = current_brightness[0]
        new_brightness = min(100, current_brightness + 10)
        sbc.set_brightness(new_brightness)
        print(f"Brightness increased to {new_brightness}%.")
        return new_brightness
    except Exception as e:
        print(f"Error adjusting brightness: {e}")
        return None
