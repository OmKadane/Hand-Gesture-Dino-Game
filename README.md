# 🦖 Hand Gesture Dino Game Controller

Control the Google Chrome Dino game using simple **hand gestures** via your webcam!

This project uses **Python**, **OpenCV**, and **CVZone** to detect a fist gesture and simulate a **spacebar keypress**, making the Dino jump—no keyboard needed!

---

## 🔧 Tech Stack
- Python 3.x
- OpenCV
- CVZone (Hand Tracking Module)
- PyAutoGUI (for keyboard control)

---

## 🎮 How It Works

- ✋ **Open Hand** → Do nothing
- ✊ **Fist Gesture (All fingers down)** → Simulates `Spacebar` press to jump
- 🙅 **No Hand Detected** → Releases the key automatically

Real-time detection with high accuracy and responsive key simulation.

---

## 📦 Installation

```bash
pip install opencv-python cvzone pyautogui

▶️ How to Run
1. Clone the repo:
```bash
https://github.com/OmKadane/Hand-Gesture-Dino-Game.git
cd Hand-Gesture-Dino-Game

2. Run the controller
```bash
python dino_gesture_controller.py

Note: Make sure keyboard_control.py is in the same directory.
