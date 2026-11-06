
class Transport:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return "Транспортний засіб"

    def __str__(self):
        return f"{self.brand}, {self.year} рік"
    
class Car(Transport):
    def __init__(self, brand, year, fuel):
        super().__init__(brand, year)
        self.fuel = fuel

    def info(self):
        return f"Автомобіль, тип палива: {self.fuel}"


class Bus(Transport):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def info(self):
        return f"Автобус, кількість місць: {self.seats}"


class Motorcycle(Transport):
    def __init__(self, brand, year, engine):
        super().__init__(brand, year)
        self.engine = engine

    def info(self):
        return f"Мотоцикл, об'єм двигуна: {self.engine} см3"
    
vehicles = [
    Car("Toyota", 2018, "бензин"),
    Bus("Mercedes", 2015, 42),
    Motorcycle("Honda", 2021, 650)
]

for vehicle in vehicles:
    print(vehicle)
    print(vehicle.info())
    print()

print("Перевірка типів:")
print("Car є Transport:", issubclass(Car, Transport))
print("Перший об'єкт є Car:", isinstance(vehicles[0], Car))
print("Другий об'єкт є Transport:", isinstance(vehicles[1], Transport))
