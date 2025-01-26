def detect_vehicles(image_path):
    import torch
    from PIL import Image
    # Load the pre-trained YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    special_vehicles = ["ambulance", "fire truck", "truck"]

    # Load the image
    image = Image.open(image_path)

    # Perform object detection
    results = model(image)

    # Extract detection results
    detections = results.pandas().xyxy[0]  # Bounding box predictions as a DataFrame

    # Filter for vehicles and ambulances
    vehicle_classes = ['car', 'truck', 'bus', 'motorbike']
    vehicle_count = 0
    sp_count = 0

    for _, row in detections.iterrows():
        if row['name'] in vehicle_classes:
            vehicle_count += 1
        if row['name'] in special_vehicles:
            sp_count += 1

    return vehicle_count, sp_count

def detect_people(image_path):
    from ultralytics import YOLO
    import cv2

    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt")  # YOLOv8 Nano pre-trained model

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found. Please check the path.")

    # Perform inference
    results = model(image)

    # Count the number of people detected (class ID for "person" is 0 in COCO dataset)
    people_count = sum(1 for result in results[0].boxes if result.cls == 0)

    return people_count


def test(image_path1, image_path2):
    v, s = detect_vehicles(image_path1)
    print(f"Number of vehicles: {v}")
    print(f"Number of special vehicles: {s}")
    people_count = detect_people(image_path2)
    print(f"Number of people is : {people_count}")

if __name__ == "__main__":
    # test("C:\\Users\\dell\\Downloads\\A.jpg")
    pass
