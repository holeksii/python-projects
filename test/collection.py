import json
from CarReservation import CarReservation as CR
from datetime import timedelta
import datetime

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


    def add(self, lst):
        self.car_reservations.append(CR.from_list(lst))


    @classmethod
    def from_json(cls, filename=FILEPATH):
        objFile = open(filename, "r")
        text = objFile.read()
        data = json.loads(text)



        lst_of_cars = []
        i = 0
        for i in range(len(data)):
            dict = data[i]
            lst_of_items = []
            for dict_item in dict.values():
                lst_of_items.append(dict_item)


            try:
                if lst_of_items[0] in list(dict.values())[1:]:
                    
                    raise ValueError("the same id")
                    print("WTF")
                # print(lst_of_items[0])
                # print(list(dict.values())[1:])
                car = CR.from_list(lst_of_items)
                lst_of_cars.append(car)
            except Exception as e:
                pass

                # errors = CR.get_errors(lst_of_items)
                # print(f'errors in CAR RESERVATION {i}')
                # for error in errors:
                #     print(error)
            i += 1
            

        objFile.close()
        
        return cls(lst_of_cars)
    
    
    def __str__(self):
        st = ""
        for i in range(len(self._car_reservations)):
            st += f'CAR RESERVATION {i}:\n\n'
            st += self._car_reservations[i].__str__()
            st += 2 * '\n'
        return st


    def dump_to_json(self):
        dicts = self.ads_to_dict()
        with open(self.FILEPATH, "w") as outfile: 
            json.dump(dicts, outfile, indent=4)
    

    def max_spending_person_by_year(self):
        maxs = 0
        today = datetime.datetime.now()

        for p in self.car_reservations:
            if p.price > maxs and (today - p.end_datetime).days < 365:
                maxs = p.price

        ret = []
        for p in self.car_reservations:
            if p.price == maxs and (today - p.end_datetime).days < 365:
                ret.append(p.name)

        return ret


    def idkhowtonamethis(self):
        carsD = {CR.cars[i]:0  for i in range(0, len(CR.cars))}
        today = datetime.datetime.now()
        for p in self.car_reservations:
            if (today - p.end_datetime).days < 365:
                if p.start_datetime < today - timedelta(days=365):
                    carsD[p.car] += (p.end_datetime - (today - timedelta(days=365))).days
                else:
                    carsD[p.car] += (p.end_datetime -p.start_datetime).days
        
        return carsD
