import cv2
from cursor_movement import handle_cursor_control
from hand_gesture import handle_gesture_control
import mediapipe as mp
import numpy as np
import time

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1)

mode = "cursor"  
last_switch_time = 0
switch_cooldown = 1.5  # Cooldown period in seconds to avoid accidental switching

# For smooth text display
display_text = "Cursor Movement Active"
last_action_time = 0
display_duration = 1.5 


def is_thumbs_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks[mp_hands.HandLandmark.THUMB_MCP]

    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    # Thumb should be pointing upwards, and other fingers should be curled
    thumb_straight = thumb_tip.y < thumb_ip.y < thumb_mcp.y
    fingers_curled = (index_tip.y > thumb_mcp.y and
                      middle_tip.y > thumb_mcp.y and
                      ring_tip.y > thumb_mcp.y and
                      pinky_tip.y > thumb_mcp.y)
    
    return thumb_straight and fingers_curled


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()

    # Check for thumb up gesture to switch mode
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_thumbs_up(hand_landmarks.landmark):
                if (current_time - last_switch_time) > switch_cooldown:
                    mode = "gesture" if mode == "cursor" else "cursor"
                    last_switch_time = current_time
                    last_action_time = current_time

    if mode == "cursor":
        handle_cursor_control(frame, results)
        if (current_time - last_action_time) > display_duration:
            display_text = "Cursor Movement Active"
    elif mode == "gesture":
        gesture_action = handle_gesture_control(frame, results)
        if gesture_action:
            display_text = f"Gesture Detected: {gesture_action}"
            last_action_time = current_time

    cv2.putText(frame, display_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Hand Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
