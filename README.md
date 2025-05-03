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
