from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8n-face.pt")

cap = cv2.VideoCapture(0)

second = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    inference_time = time.time()
    results = model(frame)
    end_inference_time = time.time()
    difference = abs(inference_time-end_inference_time)

    boxes = results[0].boxes

    if not ret:
        continue

    noObject = True

    for box in boxes:
        top_left_x = int(box.xyxy.tolist()[0][0])
        top_left_y = int(box.xyxy.tolist()[0][1])
        buttom_right_x = int(box.xyxy.tolist()[0][2])
        buttom_right_y = int(box.xyxy.tolist()[0][3])

        if isinstance(top_left_x, int):
            noObject = False
            end_time = time.time()
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.putText(frame, f'{str(round(end_time - start_time))}s', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
            second += 1

        cv2.rectangle(frame, (top_left_x, top_left_y), (buttom_right_x, buttom_right_y), (50, 200, 129), 2)

    if noObject:
        second = 0
        start_time = time.time()
        cv2.putText(frame, "NOT FOUND!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("video frame", frame)
    key_pressed = cv2.waitKey(1) & 0xFF

    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
