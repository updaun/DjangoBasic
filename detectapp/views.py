import threading

from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2

# Create your views here.
from django.views.decorators import gzip

import mediapipe as mp
import numpy as np
from PIL import Image
# import HolisticModule
# detector = HolisticModule.HolisticDetector()



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
        # image = HolisticModule.HolisticDetector().findHolistic(image, draw=True)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    # mp_drawing = mp.solutions.drawing_utils
    # mp_holistic = mp.solutions.holistic
    # mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
    while True:
        frame = camera.get_frame()
        # with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        #     image = camera.get_frame()
        #
        #     # Recolor Feed
        #     # image = Image.open(image)
        #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #     # Make Detections
        #     results = holistic.process(image)
        #     # print(results)
        #     # Recolor image back to BGR for rendering
        #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #
        #     # Draw face Landmarks
        #     # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
        #     # Right hand
        #     mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        #     # Left hand
        #     mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        #     # Pose Detections
        #     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        #
        #     image = np.array(image, dtype='uint8')
        #     # image = Image.fromarray(image)
        #     # image = cv2.imencode('.jpg', image)
        #     _, jpeg = cv2.imencode('.jpg', image)
        #     # print(type(image))
        #     print(type(jpeg))
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def detectme(request):
    try:
        img = VideoCamera()
        return StreamingHttpResponse(gen(img), content_type='multipart/x-mixed-replace;boundary=frame')

    except:
        print("Error")
        pass