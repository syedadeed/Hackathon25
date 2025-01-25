from backend.lane_class import Lane
from random import randint
from time import sleep

primary_lanes = [Lane("Lane A"), Lane("Lane B"), Lane("Lane C")]
# secondary_lanes = [Lane("LA"), Lane("LB"), Lane("LC")]

def initialize_lane(lanes: list[Lane]) -> None:
    activated_lane = randint(0, 2)
    for index, lane in enumerate(lanes):
        lane.vehicle_num = randint(0, 6)
        if randint(7, 10) == 8:
            lane.special_vehicle_count = randint(1, 3)
        if index == activated_lane:
            lane.active_time = 1
        if lane.vehicle_num == 0:
            lane.empty_time = 1
        lane.vehicle_num += lane.special_vehicle_count

def update_lane(lanes: list[Lane]) -> None:
    for lane in lanes:
        if lane.active_time > 0:
            if lane.vehicle_num > 1:
                lane.vehicle_num -= randint(1, lane.vehicle_num)
            else:
                lane.vehicle_num -= 1
            if lane.special_vehicle_count > 1:
                lane.special_vehicle_count -= randint(1, lane.special_vehicle_count)
            else:
                lane.special_vehicle_count -= 1
            lane.active_time += 1

        lane.vehicle_num += randint(0, 2)
        if randint(7, 10) == 8:
            lane.special_vehicle_count += randint(0, 1)

        if lane.special_vehicle_count < 0:
            lane.special_vehicle_count = 0
        if lane.vehicle_num < 0:
            lane.vehicle_num = 0

        lane.vehicle_num += lane.special_vehicle_count

        if lane.vehicle_num == 0:
            lane.empty_time += 1

def get_new_active_lane(lanes: list[Lane]) -> Lane:
    # Priority weights for decision-making
    special_vehicle_weight = 10  # Priority boost for special vehicles
    empty_time_penalty = -1      # Penalty for being empty recently
    active_time_penalty = -0.5

    # Initialize a priority score for each lane
    lane_scores = []

    for lane in lanes:
        score = lane.vehicle_num  # Start with the number of vehicles

        # Add a large weight if there are special vehicles in the lane
        score += lane.special_vehicle_count * special_vehicle_weight

        # Penalize lanes that have been empty recently
        score += lane.empty_time * empty_time_penalty

        # Avoid reactivating the current active lane unless necessary
        score += (lane.active_time / 5) * active_time_penalty

        lane_scores.append((lane, score))

    # Sort lanes by their score (higher is better), breaking ties by vehicle count
    lane_scores.sort(key=lambda x: (x[1], x[0].vehicle_num), reverse=True)

    # Return the lane with the highest score
    return lane_scores[0][0]

def change_lane(lanes: list[Lane]) -> None:
    current_active_lane = lanes[0]
    for lane in lanes:
        if lane.active_time > 0:
            current_active_lane = lane
            break
    new_active_lane = get_new_active_lane(lanes)
    if new_active_lane != current_active_lane:
        current_active_lane.active_time = 0
        new_active_lane.active_time = 1
    else:
        current_active_lane.active_time += 1

def print_lanes(lanes: list[Lane]) -> None:
    active_lane = lanes[0]
    for lane in lanes:
        if lane.active_time > 0:
            active_lane = lane
            break
    for i in range(len(lanes)):
        print(lanes[i].name)
        print(f"\tLane vehicles: {lanes[i].vehicle_num}")
        print(f"\tNumber of Emergency vehicles in lane: {lanes[i].special_vehicle_count}")
    print(f"New Active Lane: {active_lane}")
    print("###################################################", end="")

initialize_lane(primary_lanes)
sleep(0.1)

print("###################################################")
while True:
    print_lanes(primary_lanes)
    update_lane(primary_lanes)
    sleep(0.1)
    change_lane(primary_lanes)
    sleep(0.1)
    input()
