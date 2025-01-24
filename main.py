class Lane:
    def __init__(self, lane_name: str) -> None:
        self.name:str = lane_name
        self.vehicle_num: int = 0
        self.special_vehicles: list[str] = []  # List of special vehicles like ambulance etc
        self.is_active: bool = False
        self.active_time: int = 0
        self.empty_time: int = 0

    def __str__(self) -> str:
        return self.name

def get_new_active_lane(lanes: list[Lane], current_active: Lane) -> Lane:
    """
    TODO: Return the lane that should get activated from the "lanes" list

    The update function takes a list of lane objects(ie a list of instances of the Lane class)
    and the currently active lane

    You can get the number of vehicles in a lane using the vehicle_num attribute
    the special_vehicles attribute is a list of special vehicle names present in a lane
    the active_time attribute tells for how long the lane has been active
    the empty_time attribute tells for how long the lane has been empty
    """
