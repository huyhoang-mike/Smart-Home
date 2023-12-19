import os

from ultralytics import YOLO
import cv2

import numpy as np
import easyocr

# Load a model
model = YOLO('best.pt')  # load a custom model

# results = model.predict(source='0', show=True)
# print(results)


threshold = 0.5
webcam = cv2.VideoCapture(0)
ret = True
while ret:
    ret, frame = webcam.read()
    results = model(frame)[0]
    
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cropped_image = gray[int(y1):int(y2), int(x1):int(x2)]
            reader = easyocr.Reader(['en'])
            result = reader.readtext(cropped_image)
            
            text = ''
            for name in result:
                text += str(name[1])

            if text == 'DSF478':
                cv2.putText(frame, text.upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame, text.upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 0, 0), 3, cv2.LINE_AA)
            
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
