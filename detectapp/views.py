import threading

from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2

# Create your views here.
from django.views.decorators import gzip

import mediapipe as mp
import numpy as np

import modules.HolisticModule as hm

# detector = HolisticModule.HolisticDetector()

# image = HolisticModule.HolisticDetector().findHolistic(image, draw=True)

def camview(request):
    return render(request, 'detectapp/camview.html')

def holistic(request):
    return render(request, 'detectapp/holistic.html')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def get_image(self):
        image = self.frame
        return image

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def detectHolistic(camera):
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    mp_drawing.DrawingSpec(color=(200, 220, 30), thickness=2, circle_radius=1)
    while True:
        # frame = camera.get_frame()
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            image = camera.get_image()

            # Recolor Feed
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Make Detections
            results = holistic.process(image)
            # Recolor image back to BGR for rendering
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw face Landmarks
            # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
            # Right hand
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            # Left hand
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            # Pose Detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            image = np.array(image, dtype='uint8')

            _, image = cv2.imencode('.jpg', image)

            image = image.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')

@gzip.gzip_page
def detectme(request):
    try:
        img = VideoCamera()
        return StreamingHttpResponse(detectHolistic(img), content_type='multipart/x-mixed-replace;boundary=frame')

    except:
        print("Error")
        pass

@gzip.gzip_page
def opencamera(request):
    try:
        img = VideoCamera()
        return StreamingHttpResponse(gen(img), content_type='multipart/x-mixed-replace;boundary=frame')

    except:
        print("Error")
        pass