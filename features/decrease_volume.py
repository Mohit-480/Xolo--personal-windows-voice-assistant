from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def decrease_volume():
    """Decrease system volume by 10%, down to a minimum of 0%."""
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()  # Current volume as scalar (0.0 to 1.0)
        new_volume = max(0.0, current_volume - 0.1)  # Ensure volume doesn't go below 0%
        volume.SetMasterVolumeLevelScalar(new_volume, None)  # Set new volume level
        percentage_volume = int(new_volume * 100)  # Convert scalar to percentage
        print(f"Volume decreased to {percentage_volume}%.")
        return percentage_volume
    except Exception as e:
        print(f"Error adjusting volume: {e}")
        return None
