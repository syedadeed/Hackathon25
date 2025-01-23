import torch
import cv2
import numpy as np

def count_vehicles(image_path):
    # Load YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at path: {image_path}")
    
    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Perform inference
    results = model(img_rgb)
    
    # Filter for vehicle classes (car, truck, bus, motorcycle)
    vehicle_classes = ['car', 'truck', 'bus', 'motorcycle']
    vehicle_count = 0
    
    # Get detections
    detections = results.pandas().xyxy[0]
    
    # Count vehicles
    for _, detection in detections.iterrows():
        if detection['name'] in vehicle_classes and detection['confidence'] > 0.5:
            vehicle_count += 1
    
    return vehicle_count



image_path = "C:\\Users\\dell\\OneDrive\\Desktop\\test.jpg"
num_vehicles = count_vehicles(image_path)
print(f"Number of vehicles detected: {num_vehicles}")