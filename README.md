# Sleep Detector

A small Flask web app that detects eyes and faces from a webcam feed using OpenCV Haar cascades. The app can be used as a simple sleep/drowsiness detection demo.

## Features
- Live webcam video capture
- Face and eye detection using Haar cascade models
- Simple Flask-based UI served from `templates/index.html`

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies

## Quickstart
1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Run `setup_cascades.py` if you need to re-download or verify cascade files.

4. Start the app:

   ```bash
   python sleep-detector/app.py
   ```

5. Open your browser to http://127.0.0.1:5000/ to view the UI.

## Files of interest
- `sleep-detector/app.py` — main Flask application and detection logic
- `sleep-detector/setup_cascades.py` — helper to prepare Haar cascade files
- `sleep-detector/haarcascade_frontalface_default.xml` — face cascade (included)
- `sleep-detector/haarcascade_eye.xml` — eye cascade (included)
- `sleep-detector/templates/index.html` — simple front-end
- `sleep-detector/static/style.css` — styles for the UI

## Troubleshooting
- If the webcam cannot be accessed, ensure no other app is using it and that camera permissions are granted.
- If detection is poor, try different lighting or move the camera closer to the subject.

## License
This project is provided as-is for learning and demo purposes. Add a license file if you want to publish it.

## Acknowledgements
- Built with OpenCV and Flask.
