from flask import Flask, render_template, Response, jsonify
import cv2
import time
import os

app = Flask(__name__)
alert_active = False

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

camera = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(os.path.join(script_dir, "haarcascade_eye.xml"))
face_cascade = cv2.CascadeClassifier(os.path.join(script_dir, "haarcascade_frontalface_default.xml"))

eye_close_time = None

def gen_frames():
    global eye_close_time, alert_active
    while True:
        success, frame = camera.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        
        # Draw face rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Draw eye rectangles
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if len(eyes) == 0:
            if eye_close_time is None:
                eye_close_time = time.time()
            elif time.time() - eye_close_time > 3:
                alert_active = True
                # Draw ALERT text on frame
                cv2.putText(frame, "ALERT: DROWSINESS DETECTED!", (50, 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            eye_close_time = None
            alert_active = False

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/alert-status')
def alert_status():
    global alert_active
    return jsonify({"alert": alert_active})

if __name__ == "__main__":
    app.run(debug=True)
