import pyautogui
from datetime import datetime
from PIL import Image

def take_full_screenshot(save_path="screenshots/fullscreen.png"):
    """Capture the full screen and save it."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_path.split('.')[0]}_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

