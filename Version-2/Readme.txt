**Air Gesture Control (Version 2)**

This project expands upon Version 1 by introducing mouse control functionalities using hand gestures.

**How it Works:**

* **Hand Detection:** Utilizes MediaPipe to detect and track hand landmarks in real-time.
* **Gesture Recognition:** Interprets specific hand postures (index finger, thumb, and both) to determine desired actions.
* **Cursor Control:** Maps hand movements to cursor movements on the screen, incorporating smoothing techniques for accuracy.
* **Click Simulation:** Detects specific finger combinations to simulate mouse clicks.
* **System Integration:** Interacts with the operating system to move the cursor and trigger click events.

**Requirements:**

* Python 3.x
* OpenCV library
* MediaPipe library
* AutoPy library (for mouse control)
* PyCaw library (for Windows volume control)
* win10toast library (for Windows 10 notifications)

**Installation:**

1. Install Python 3.x from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open a terminal window and navigate to your project directory.
3. Install the required libraries using pip:

```bash
pip install opencv-python mediapipe autopy pycaw win10toast
```

**Running the Script:**

1. Open a terminal window and navigate to your project directory.
2. Run the script using the following command:

```bash
python Mousecontrol.py
```

**Explanation of Files:**

* HandDetection.py: Contains functions for hand detection and tracking.
* Mousecontrol.py: The main script that controls mouse movement and click actions based on hand gestures.
* requirements.txt: A text file that lists the required Python libraries for the project.
* Readme.txt: This file (the one you are reading now).

**Note:**

* This version builds upon Version 1 by adding mouse control features.
* The code uses deprecation warnings (`warnings.filterwarnings("ignore")`). It's recommended to address these warnings in future versions.

**Future Improvements:**

* Refine gesture recognition for better accuracy and responsiveness.
* Explore additional hand gestures for more complex actions.
* Improve system performance for smoother operation.
```

