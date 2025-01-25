from tkinter import *
from backend.lane_class import Lane
from backend.lane_funcs import *

lanes = [Lane("Lane A"), Lane("Lane B"), Lane("Lane C")]
initialize_lane(lanes)

root = Tk()

background_image = PhotoImage(file="assets/bg.png")

lane_status_image = PhotoImage(file="assets/stop_sign.png")

car_image_A = PhotoImage(file="assets/car_A.png")
special_vehicle_image_A = PhotoImage(file="assets/sp_A.png")

car_image_B = PhotoImage(file="assets/car_B.png")
special_vehicle_image_B = PhotoImage(file="assets/sp_B.png")

car_image_C = PhotoImage(file="assets/car_C.png")
special_vehicle_image_C = PhotoImage(file="assets/sp_C.png")

Label(root, image=background_image).place(x=-100, y=-10)

def update_lane_A(vehicle_num: int, special_vehicle_num: int, active_status: bool) -> list[Label]:
    labels = []

    y_coords = 270
    for i in range(special_vehicle_num):
        x = Label(root, image=special_vehicle_image_A)
        labels.append(x)
        x.place(x=690, y=y_coords)
        y_coords += 60

    for i in range(vehicle_num):
        x = Label(root, image=car_image_A)
        labels.append(x)
        x.place(x=690, y=y_coords)
        y_coords += 60

    if not active_status:
        x = Label(root, image=lane_status_image)
        labels.append(x)
        x.place(x=690, y=170)
    return labels


def update_lane_B(vehicle_num: int, special_vehicle_num: int, active_status: bool):
    labels = []

    x_coords = 500
    for i in range(special_vehicle_num):
        x = Label(root, image=special_vehicle_image_B)
        labels.append(x)
        x.place(x=x_coords, y=90)
        x_coords -= 60

    for i in range(vehicle_num):
        x = Label(root, image=car_image_B)
        labels.append(x)
        x.place(x=x_coords, y=90)
        x_coords -= 60

    if not active_status:
        x = Label(root, image=lane_status_image)
        labels.append(x)
        x.place(x=600, y=90)
    return labels

def update_lane_C(vehicle_num: int, special_vehicle_num: int, active_status: bool):
    labels = []

    x_coords = 900
    for i in range(special_vehicle_num):
        x = Label(root, image=special_vehicle_image_C)
        labels.append(x)
        x.place(x=x_coords, y=90)
        x_coords += 60

    for i in range(vehicle_num):
        x = Label(root, image=car_image_C)
        labels.append(x)
        x.place(x=x_coords, y=90)
        x_coords += 60

    if not active_status:
        x = Label(root, image=lane_status_image)
        labels.append(x)
        x.place(x=800, y=90)
    return labels

labels:list[Label] = []

while True:
    for i in labels:
        i.destroy()
    labels.extend(update_lane_A(lanes[0].vehicle_num - lanes[0].special_vehicle_count, lanes[0].special_vehicle_count, True if lanes[0].active_time > 0 else False))
    labels.extend(update_lane_B(lanes[1].vehicle_num - lanes[1].special_vehicle_count, lanes[1].special_vehicle_count, True if lanes[1].active_time > 0 else False))
    labels.extend(update_lane_C(lanes[2].vehicle_num - lanes[2].special_vehicle_count, lanes[2].special_vehicle_count, True if lanes[2].active_time > 0 else False))
    update_lane(lanes)
    change_lane(lanes)
    root.update()
    input()
