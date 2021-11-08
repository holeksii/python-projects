from collection import Collection as C
from CarReservation import CarReservation as CR


c=C.from_json()
c.add([12345, "Ford Fiesta", "2020-01-01 10:00", "2020-01-02 09:00", "Alex", 562])
print(c.idkhowtonamethis())
print(c.max_spending_person_by_year())