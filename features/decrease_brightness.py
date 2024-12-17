import screen_brightness_control as sbc

def decrease_brightness():
    """Decrease screen brightness by 10%, down to a minimum of 0%."""
    try:
        current_brightness = sbc.get_brightness()
        if isinstance(current_brightness, list):
            current_brightness = current_brightness[0]
        new_brightness = max(0, current_brightness - 10)
        sbc.set_brightness(new_brightness)
        print(f"Brightness decreased to {new_brightness}%.")
        return new_brightness
    except Exception as e:
        print(f"Error adjusting brightness: {e}")
        return None
