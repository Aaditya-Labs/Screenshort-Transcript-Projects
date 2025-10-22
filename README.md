## PROJECTS 
# 🖼️ Screenshot Capture and Text Extraction API

This project is a **Python-based application** that can capture screenshots (full-screen or rectangular region) and automatically extract all readable text from the captured image using **Optical Character Recognition (OCR)**.  
It provides both a **Flask API** for automation and a **Tkinter GUI** for user-friendly interaction.

---

## 🚀 Features
- 📸 Capture full-screen or custom rectangular screenshots  
- 🔠 Extract text automatically using Tesseract OCR  
- 🌐 REST API built with Flask  
- 🖥️ Simple graphical interface built with Tkinter  
- 💾 Automatically saves all screenshots locally  
- ⚙️ Works across major operating systems (Windows, macOS, Linux)

---

## 🏗️ Project Structure
```
Screenshot_Text_Extraction_API/
│
├── main.py              # Launches both API and GUI
├── api.py               # Flask API endpoints for screenshots & OCR
├── gui.py               # GUI interface for capturing screenshots
├── fullscreenshot.py    # Full-screen capture logic
├── rectangular.py       # Rectangular (custom area) capture logic
└── requirements.txt     # Project dependencies
```

---

## 🧰 Technologies Used
- **Python 3.x**
- **Flask** – REST API creation
- **PyAutoGUI** – Screenshot capture
- **Pillow (PIL)** – Image processing
- **OpenCV** – Image enhancement and preprocessing
- **PyTesseract** – OCR (Optical Character Recognition)
- **Tkinter** – GUI framework for desktop interface

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aaditya-Labs/Screenshot_Text_Extraction_API.git
cd Screenshot_Text_Extraction_API
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python main.py
```
- The GUI window will open.
- Flask API will run at `http://127.0.0.1:5000`.

---

## 🌐 API Endpoints

### 1. Capture Full Screen
**GET** `/capture/full`  
→ Captures the entire screen and extracts text.

**Response:**
```json
{
  "screenshot": "screenshots/fullscreen_20251022_153045.png",
  "extracted_text": "Detected text from screen..."
}
```

### 2. Capture Rectangular Area
**POST** `/capture/rectangle`  
→ Captures a specific screen region and extracts text.

**Example Request:**
```json
{
  "x1": 100,
  "y1": 100,
  "x2": 600,
  "y2": 400
}
```

**Response:**
```json
{
  "screenshot": "screenshots/rectangle_20251022_153500.png",
  "extracted_text": "Detected text from selected region..."
}
```

---

## 🖥️ GUI Usage
1. Launch the app using `python main.py`
2. Use buttons in the window to:
   - Capture Full Screen
   - Capture Rectangular Area
   - Extract Text from Latest Screenshot
3. Extracted text will display in a popup.

---

## 🔮 Future Enhancements
- Multi-language OCR support  
- Integration with cloud storage  
- Real-time screen text detection  
- Web dashboard for managing text and screenshots  
- Improved accuracy using Deep Learning OCR models

---

## 🧑‍💻 Author
**Aditya Kumar Singh**   

---

