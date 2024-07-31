# Ignore the warnings for the time being (deprecation warnings)

import warnings
warnings.filterwarnings("ignore")

# Importing the required libraries

import cv2 
import mediapipe as mp
import sys
import time
import math
from Air_Gesture_utils import calibrated_volume_gesture, calibrated_brightness_gesture 

from win10toast import ToastNotifier # For Windows 10 Notifications

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Hyperparameters
threshold = 0.005

# Hand Settings
landmark_1_name = mp_hands.HandLandmark.THUMB_TIP
landmark_2_name = mp_hands.HandLandmark.INDEX_FINGER_TIP

# Initialize the toaster
toaster = ToastNotifier()

# Calibration Phase (Any Hand)

toaster.show_toast("Air Gesture", "\nCalibration Phase", duration=4)

min_distance = sys.float_info.max
max_distance = sys.float_info.min

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
        
        # Extract coordinates (modify based on your chosen landmark names)
        landmark_1_x = hand_landmarks.landmark[landmark_1_name].x
        landmark_1_y = hand_landmarks.landmark[landmark_1_name].y
        landmark_2_x = hand_landmarks.landmark[landmark_2_name].x
        landmark_2_y = hand_landmarks.landmark[landmark_2_name].y

        # Calculate distance
        distance = math.sqrt((landmark_2_x - landmark_1_x)**2 + (landmark_2_y - landmark_1_y)**2)

        min_distance = min(min_distance, distance)
        max_distance = max(max_distance, distance)
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('Calibration', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break


if(min_distance == sys.float_info.max or max_distance == sys.float_info.min):
  print("No hands detected. Exiting...")
  sys.exit()

# Main Phase (Volume Control and Brightness Control)

toaster.show_toast("Air Gesture", "\nControl Phase.\nLeft -> Brightness\nRight -> Volume", duration=4)

prev_distance = 0

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
        
        # Extract coordinates (modify based on your chosen landmark names)
        landmark_1_x = hand_landmarks.landmark[landmark_1_name].x
        landmark_1_y = hand_landmarks.landmark[landmark_1_name].y
        landmark_2_x = hand_landmarks.landmark[landmark_2_name].x
        landmark_2_y = hand_landmarks.landmark[landmark_2_name].y

        # Calculate distance
        distance = math.sqrt((landmark_2_x - landmark_1_x)**2 + (landmark_2_y - landmark_1_y)**2)

        # Extract handedness from the results
        handedness = results.multi_handedness[0].classification[0].label

        if(handedness == "Left"): 
          calibrated_volume_gesture(distance, min_distance, max_distance, 0, 100)
        else:
          calibrated_brightness_gesture(distance, min_distance, max_distance, 0, 100)

        time.sleep(0.1)
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('Air Gesture', cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == ord('q'):
      cap.release()
      cv2.destroyAllWindows()
      break