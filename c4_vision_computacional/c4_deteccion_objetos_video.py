import  cv2
import cvzone
import math
import os

from ultralytics import YOLO


model = YOLO('yolov8n.pt')
class_names = model.names

video_path = os.path.join(os.getcwd(), "escritorio.mp4")
capture = cv2.VideoCapture(video_path)

while capture.isOpened():
    success, image = capture.read()

    if not success:
        print("No frame available to process.")
        break

    model_results = model(image, stream=True)
    for result in model_results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            width = x2 - x1
            height = y2 - y1
            cvzone.cornerRect(image, (x1, y1, width, height))

            conf = math.ceil((box.conf[0]*100))/100

            cls = box.cls[0]
            name = class_names[int(cls)]

            cvzone.putTextRect(
                img=image,
                text=f'{name} {conf}',
                pos=(max(0,x1), max(35,y1)),
                colorR=(255, 0, 0)
            )

    cv2.imshow("Image", image)
    cv2.waitKey(1)
