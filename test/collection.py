import json
from CarReservation import CarReservation as CR

class Collection:
    FILEPATH = "data/reservations.json"


    def __init__(self, car_reservations) -> None:
        self.car_reservations = car_reservations

    @property
    def car_reservations(self):
        return self._car_reservations

    @car_reservations.setter
    def car_reservations(self, cars):
        if not isinstance(cars, list):
            raise TypeError("invalid list of car_reservations")
        self._car_reservations = cars

    
    


    
