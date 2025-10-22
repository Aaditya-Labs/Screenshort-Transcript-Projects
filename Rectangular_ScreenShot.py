import pyautogui
from datetime import datetime

def take_rectangular_screenshot(x1, y1, x2, y2, save_path="screenshots/rectangle.png"):
    """Capture a rectangular region of the screen."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_path.split('.')[0]}_{timestamp}.png"
    region = (x1, y1, x2 - x1, y2 - y1)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)
    return filename
