import threading
from gui import run_gui
from api import app
import os

if __name__ == "__main__":
    os.makedirs("screenshots", exist_ok=True)
    
    # Run both GUI and API concurrently
    threading.Thread(target=lambda: app.run(debug=False, port=5000)).start()
    run_gui()

