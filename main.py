class Lane:
    def __init__(self, lane_name) -> None:
        self.name = lane_name
        self.vehicle_num: int = 0
        self.special_vehicles: list[str] = []  # List of special vehicles like ambulance etc
        self.is_active: bool = False

def update(lanes: list[Lane], current_active: Lane) -> Lane:
    """
    The update function takes a list of lane objects(ie a list of instances of the Lane class)
    TODO: Return the lane that should be active from the lanes list
    You can get the number of vehicles of a lane using the vehicle_num attribute
    """
