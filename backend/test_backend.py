from time import sleep
from lane_funcs import *

primary_lanes = [Lane("Lane A"), Lane("Lane B"), Lane("Lane C")]
# secondary_lanes = [Lane("LA"), Lane("LB"), Lane("LC")]

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
