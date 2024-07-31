# Ignore the warnings for the time being (deprecation warnings)
import warnings
warnings.filterwarnings("ignore")

from comtypes import CLSCTX_ALL
import wmi
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Volume Control Initialization

try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
except Exception as e:
    print(f"Error initializing volume control: {e}")

# Create a WMI object (Brightness Control)

try:
    wmi_obj = wmi.WMI(namespace='wmi')
    brightness_methods = wmi_obj.WmiMonitorBrightnessMethods()[0]
except Exception as e:
    print(f"Error initializing brightness control: {e}")

# Define the functions for Volume Control and Brightness Control

def calibrated_volume_gesture(x, in_min, in_max, out_min, out_max):
    percentage = int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)/100

    if percentage < 0:
        percentage = 0
    elif percentage > 1:
        percentage = 1

    try:
        volume.SetMasterVolumeLevelScalar(percentage, None)
    except Exception as e:
        print(f"Error setting volume: {e}")

def calibrated_brightness_gesture(x, in_min, in_max, out_min, out_max):
    percentage = int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100

    try:
        brightness_methods.WmiSetBrightness(percentage, 0)
    except Exception as e:
        print(f"Error setting brightness: {e}")