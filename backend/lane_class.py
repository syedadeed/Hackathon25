class Lane:
    def __init__(self, lane_name: str, vehicle_num:int = 0, special_vehicle_count: int = 0, active_time: int = 0, empty_time: int = 0) -> None:
        self.name:str = lane_name
        self.vehicle_num: int = vehicle_num
        self.special_vehicle_count = special_vehicle_count
        self.active_time: int = active_time
        self.empty_time: int = empty_time

    def __str__(self) -> str:
        return self.name
