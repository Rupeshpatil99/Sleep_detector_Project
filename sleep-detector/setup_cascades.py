import cv2
import os

# Get cascade classifier paths from OpenCV installation
cascade_path = cv2.data.haarcascades

eye_cascade_src = os.path.join(cascade_path, 'haarcascade_eye.xml')
face_cascade_src = os.path.join(cascade_path, 'haarcascade_frontalface_default.xml')

script_dir = os.path.dirname(os.path.abspath(__file__))

# Copy cascade files to project directory
import shutil

if os.path.exists(eye_cascade_src):
    shutil.copy(eye_cascade_src, os.path.join(script_dir, 'haarcascade_eye.xml'))
    print(f"Copied eye cascade from {eye_cascade_src}")
else:
    print(f"Eye cascade not found at {eye_cascade_src}")

if os.path.exists(face_cascade_src):
    shutil.copy(face_cascade_src, os.path.join(script_dir, 'haarcascade_frontalface_default.xml'))
    print(f"Copied face cascade from {face_cascade_src}")
else:
    print(f"Face cascade not found at {face_cascade_src}")

print("Setup complete!")
