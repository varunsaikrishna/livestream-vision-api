from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
def process(frame): return model(frame)