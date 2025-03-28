# AirPointer

## Overview
AirPointer is a real-time hand gesture-based cursor and browser navigation system. It leverages **MediaPipe** to track hand landmarks and uses **PyAutoGUI** to perform seamless navigation and cursor control without the need for physical input devices. This system enables hands-free interaction, making it useful for accessibility, touchless control, and immersive experiences.

## Features
- **Real-time Hand Tracking:** Uses MediaPipe to detect and track hand landmarks.
- **Cursor Control:** Navigate the cursor using hand gestures.
- **Click & Scroll:** Perform left-click, right-click, and scrolling actions with specific hand gestures.
- **Browser Navigation:** Seamlessly switch between tabs, refresh, open, and close tabs with intuitive gestures.
- **Mode Switching:** Toggle between cursor movement and browser navigation mode using a thumbs-up gesture.
- **Hands-Free Interaction:** Enables touchless control for accessibility and convenience.

## Gesture Controls
### **Browser Navigation Mode**
- **Index Finger Left:** Navigate to the previous tab.
- **Index Finger Right:** Navigate to the next tab.
- **Open Palm:** Open a new tab.
- **Closed Palm:** Close the current tab.
- **Victory Sign:** Refresh the current tab.
- **Three Fingers Up:** Scroll up.
- **Hang Loose Gesture:** Scroll down.
- **Thumbs-Up Gesture:** Toggle between cursor movement and browser navigation mode.

### **Cursor Navigation Mode**
- **Index Finger Movement:** Move the cursor.
- **Okay Sign:** Left-click.
- **Double-Finger Okay Sign:** Right-click.
- **Double Tap Okay Sign:** Double-click.

## Technologies Used
- **Python**
- **MediaPipe** (for hand tracking)
- **OpenCV** (for video processing)
- **PyAutoGUI** (for controlling the mouse and browser navigation)
- **NumPy** (for efficient computations)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Sania-hasann/AirPointer.git
   cd AirPointer
   ```
2. Install the required dependencies:
   ```bash
   pip install mediapipe opencv-python pyautogui numpy
   ```
3. Run the script:
   ```bash
   python airpointer.py
   ```

## Usage Scenarios
- **Accessibility:** Provides an alternative input method for individuals with limited mobility.
- **Touchless Navigation:** Useful in public kiosks, smart homes, and hygiene-sensitive environments.
- **Immersive Interaction:** Enhances user experience in gaming, presentations, and virtual environments.
- **Automation & Productivity:** Allows fast tab switching, scrolling, and navigation without using a keyboard or mouse.

## Future Improvements
- Assign easy hand gesture for navigation.
- Enhance gesture recognition accuracy.
- Support for multiple applications beyond browsers.
- Customizable gesture mappings.
- Multi-hand gesture recognition for extended functionalities.

## Contribution
Feel free to fork this repository, raise issues, and submit pull requests!

## License
This project is licensed under the MIT License.

---
### Author: Syeda Sania Hasan

