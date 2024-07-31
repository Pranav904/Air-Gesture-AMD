**Air Gesture Control (Version 1)**

This project allows users to control their computer's volume and brightness levels using hand gestures detected through a webcam.

**How it Works:**

1. **Calibration Phase:** The system establishes a baseline for hand gesture measurements by prompting users to perform various hand movements. The distance between the thumb and index finger is captured during calibration.
2. **Control Phase:** The webcam continuously captures video frames. Hand detection and tracking algorithms locate and follow hand movements. The distance between the thumb and index finger is calculated in real-time. Based on this distance and the calibration data, the system determines whether to adjust volume or brightness.

**Requirements:**

* Python 3.x
* OpenCV library
* MediaPipe library
* pycaw library (for Windows volume control)
* win10toast library (for Windows 10 notifications)

**Installation:**

1. Install Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open a terminal window and navigate to your project directory.
3. Install the required libraries using pip:

```bash
pip install opencv-python mediapipe pycaw win10toast
```

**Running the Script:**

1. Open a terminal window and navigate to your project directory.
2. Run the script using the following command:

```bash
python Air_Gesture_Final.py
```

**Explanation of Files:**

* Air_Gesture_Final.py: The main script that controls the entire hand gesture recognition and system interaction process.
* Air_Gesture_utils.py (assumed): This file likely contains functions for volume and brightness adjustments based on calibrated gestures.
* requirements.txt: A text file that lists the required Python libraries for the project.
* Readme.txt: This file (the one you are reading now).

**Note:**

* This version only uses the distance between the thumb and index finger for control.
* The code uses deprecation warnings (`warnings.filterwarnings("ignore")`). It's recommended to address these warnings in future versions.

**Future Improvements:**

* Implement gesture recognition for more control options (e.g., mouse movement).
* Refine gesture recognition accuracy.

