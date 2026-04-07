from ultralytics import YOLO
model = YOLO("yolov8n.pt")
def stream_process(frame):
    results = model(frame)
    return results