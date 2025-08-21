from  ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model.track(frame,persist=True,tracker="bytetrack.yaml")
    annotatte_Frame=results[0].plot()

    cv2.imshow("YOLO Object Tracking", annotatte_Frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()