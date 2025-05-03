import pyautogui

# Space key press using pyautogui
space_pressed = 'space'

def PressKey(key):
    pyautogui.keyDown(key)  # Simulate pressing the key down

def ReleaseKey(key):
    pyautogui.keyUp(key)  # Simulate releasing the key up
