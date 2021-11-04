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


    @classmethod
    def from_json(cls, filename=FILEPATH):
        objFile = open(filename, "r")
        text = objFile.read()
        data = json.loads(text)



        lst_of_cars = []
        i = 0
        for dict in data:
            lst_of_items = []
            for dict_item in dict.values():
                lst_of_items.append(dict_item)
            try:
                # if lst_of_items[0] in dict.values():
                #     return
                car = CR.from_list(lst_of_items)
            except:
                return
                # errors = CR.get_errors(lst_of_items)
                # print(f'errors in CAR RESERVATION {i}')
                # for error in errors:
                #     print(error)
            i += 1
            lst_of_cars.append(car)

        objFile.close()
        
        return cls(lst_of_cars)
    
    
    def __str__(self):
        st = ""
        for i in range(len(self._car_reservations)):
            st += f'CAR RESERVATION {i}:\n\n'
            st += self._car_reservations[i].__str__()
            st += 2 * '\n'
        return st

    
c=Collection.from_json()
print(c)