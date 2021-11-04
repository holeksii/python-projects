from Validator import Validators as Vld

class CarReservation:
    cars = [ "Audi A3", "BMW X1", "Toyota Yaris", "Volkswagen T-Roc", "Ford Fiesta", "Honda Civic", "Volkswagen Golf" ]

    def __init__(self, id, car, start_datetime, end_datetime, name, price) -> None:
        self.id = id
        self.car = car
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.name = name
        self.price = price


    @property
    def id(self):
        return self._id

    @id.setter
    @Vld.ID
    def id(self, Id):
        self._id = Id

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, carr):
        if carr in self.cars:
            self._car = carr
        else:
            raise ValueError("invalid car")

    @property
    def start_datetime(self):
        return self._start_datetime

    @start_datetime.setter
    @Vld.datetime
    def start_datetime(self, dtime):
        self._start_datetime = dtime

    @property
    def end_datetime(self):
        return self._end_datetime

    @end_datetime.setter
    @Vld.datetime
    def end_datetime(self, dtime):
        self._end_datetime = dtime

    @property
    def name(self):
        return self._name

    @name.setter
    @Vld.name
    def name(self, nname):
        self._name = nname

    @property
    def price(self):
        return self._price

    @price.setter
    @Vld.currency
    def price(self, pr):
        self._price = pr
        


    @classmethod
    def from_list(cls, l):
        return cls(l[0], l[1], l[2], l[3], l[4], l[5])


    def __str__(self) -> str:
        ret = ''
        for item in self.__dict__.values():
            ret += str(item) + '\n'
        return ret