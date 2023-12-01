import cv2
from ultralytics import YOLO
import numpy as np


class Tracker:
    def __init__(self, video_path='assets/vidp.mp4', yolo_model='yolov8n.pt'):
        self.vp = video_path
        self.ymodel = yolo_model
        self.number_of_people = 0

    def setNumOfPeople(self, num):
        self.number_of_people = num

    def handleTracking(self):
        model = YOLO(self.ymodel)

        # Load video
        cap = cv2.VideoCapture(self.vp)

        ret = True
        # Read frames
        while ret:
            ret, frame = cap.read()

            # Detect Objects & Track Objects
            results = model.track(frame, persist=True)
            self.setNumOfPeople(np.asarray(results[0].boxes.id).size)

            # Plot result
            frame_ = results[0].plot()

            # Visualize
            cv2.imshow('frame', frame_)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
