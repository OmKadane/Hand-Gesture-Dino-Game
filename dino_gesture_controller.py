import cv2
from cvzone.HandTrackingModule import HandDetector
from keyboard_control import PressKey, ReleaseKey, space_pressed
import time

# Initialize hand detector with confidence and max 1 hand
detector = HandDetector(detectionCon=0.7, maxHands=1)

current_key_pressed = set()  # Track pressed keys
SPACE_KEY = space_pressed    # Key to simulate (spacebar)

# Start video capture from webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

last_detected = 0
detect_interval = 0.1  # Detection every 100ms

while True:
    ret, frame = video.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1) # Mirror image for better UX 
    current_time = time.time()

    # Detect hand at intervals
    if current_time - last_detected >= detect_interval:
        hands, img = detector.findHands(frame, draw=False)
        last_detected = current_time
    else:
        img = frame

    if hands:
        lmList = hands[0]  # Landmark list
        fingerUp = detector.fingersUp(lmList)  # Get finger status

        # All fingers down → press space
        if fingerUp == [0, 0, 0, 0, 0]:
            if SPACE_KEY not in current_key_pressed:
                PressKey(SPACE_KEY)
                current_key_pressed.add(SPACE_KEY)
        else:
            # Fingers up → release space
            if SPACE_KEY in current_key_pressed:
                ReleaseKey(SPACE_KEY)
                current_key_pressed.remove(SPACE_KEY)
    else:
        # No hand → release space
        if SPACE_KEY in current_key_pressed:
            ReleaseKey(SPACE_KEY)
            current_key_pressed.remove(SPACE_KEY)

    # Show the frame
    cv2.imshow("Hand Gesture Dino Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Exit on 'q'
        break

# Release camera and close windows
video.release()
cv2.destroyAllWindows()
