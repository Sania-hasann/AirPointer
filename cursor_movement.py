import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

smoothening = 5
prev_x, prev_y = 0, 0
last_click_time = 0
cooldown_duration = 1

def move_cursor(landmarks):
    global prev_x, prev_y
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    x = int(index_finger.x * screen_width)
    y = int(index_finger.y * screen_height)
    
    curr_x = prev_x + (x - prev_x) / smoothening
    curr_y = prev_y + (y - prev_y) / smoothening
    
    pyautogui.moveTo(curr_x, curr_y)
    prev_x, prev_y = curr_x, curr_y

def detect_clicks(landmarks):
    global last_click_time
    index_finger = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    middle_finger = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

    distance_index_thumb = np.linalg.norm(np.array([index_finger.x, index_finger.y]) - 
                                          np.array([thumb_tip.x, thumb_tip.y]))
    distance_index_middle = np.linalg.norm(np.array([index_finger.x, index_finger.y]) - 
                                           np.array([middle_finger.x, middle_finger.y]))

    click_threshold = 0.05
    current_time = time.time()

    action = None
    if distance_index_thumb < click_threshold:
        pyautogui.click()
        action = "Left Click"
    elif distance_index_middle < click_threshold and (current_time - last_click_time) > cooldown_duration:
        pyautogui.rightClick()
        last_click_time = current_time
        action = "Right Click"

    return action

def handle_cursor_control(frame, results):
    action = None
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            move_cursor(hand_landmarks.landmark)
            action = detect_clicks(hand_landmarks.landmark)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return action  
