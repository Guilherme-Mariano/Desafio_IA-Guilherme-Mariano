import cv2
from ultralytics import YOLO


class FaceBlur:
    def __init__(self, video_path='assets/testvid.mp4', yolo_model='yolov8n.pt'):
        self.NUM_OF_PEOPLE = 0
        self.PRESS_COUNT = 1
        self.model = yolo_model
        self.vp = video_path

    def handleBlur(self):
        model = YOLO(self.model)
        cap = cv2.VideoCapture(self.vp)
        ret = True

        # Read Frames
        while ret:
            ret, frame = cap.read()

            results = model.track(frame, persist=True)

            frame_ = results[0].plot(boxes=False)

            gray_frame = cv2.cvtColor(frame_, cv2.COLOR_BGR2GRAY)

            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            face = face_classifier.detectMultiScale(
                gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
            )

            for (x, y, w, h) in face:
                cv2.rectangle(frame_, (x, y), (x + w, y + h), (0, 255, 0), 4)

                if self.PRESS_COUNT % 2 == 0:
                    roi = frame_[y:y + h, x:x + w]
                    roi = cv2.GaussianBlur(roi, (23, 23), 30)
                    frame_[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

            cv2.imshow('frame', frame_)

            pressedKey = cv2.waitKey(1) & 0xFF
            if pressedKey == ord('q'):
                break
            elif pressedKey == ord('b'):
                self.PRESS_COUNT = self.PRESS_COUNT + 1

