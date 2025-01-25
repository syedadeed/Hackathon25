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

def test(image_path):
    v, s = detect_vehicles(image_path)
    print(f"Number of vehicles: {v}")
    print(f"Number of special vehicles: {s}")

if __name__ == "__main__":
    test("C:\\Users\\dell\\Downloads\\A.jpg")
