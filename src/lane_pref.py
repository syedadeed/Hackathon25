def get_new_active_lane(lanes: list[Lane]) -> Lane:
    # Priority weights for decision-making
    special_vehicle_weight = 10  # Priority boost for special vehicles
    empty_time_penalty = -1      # Penalty for being empty recently
    active_time_penalty = -1

    # Initialize a priority score for each lane
    lane_scores = []

    for lane in lanes:
        score = lane.vehicle_num  # Start with the number of vehicles

        # Add a large weight if there are special vehicles in the lane
        score += lane.special_vehicle_present * special_vehicle_weight

        # Penalize lanes that have been empty recently
        score += lane.empty_time * empty_time_penalty

        # Avoid reactivating the current active lane unless necessary
        score += (lane.active_time / 5) * active_time_penalty

        lane_scores.append((lane, score))

    # Sort lanes by their score (higher is better), breaking ties by vehicle count
    lane_scores.sort(key=lambda x: (x[1], x[0].vehicle_num), reverse=True)

    # Return the lane with the highest score
    return lane_scores[0][0]

def detect_vehicles_and_ambulance(image_path):
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
    ambulance_detected = False

    for _, row in detections.iterrows():
        if row['name'] in vehicle_classes:
            vehicle_count += 1
        if row['name'] in special_vehicles:
            ambulance_detected = True

    return vehicle_count, ambulance_detected
