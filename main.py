class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Это транспортное средство марки {self.brand}, {self.year} года выпуска")

class Car(Vehicle):
    def __init__(self, brand, year, model, doors):
        super().__init__(brand, year)
        self.model = model
        self.doors = doors

    def info(self):
        super().info()
        print(f"Это автомобиль модели {self.model} с {self.doors} дверями")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_type):
        super().__init__(brand, year)
        self.engine_type = engine_type

    def info(self):
        super().info()
        print(f"Это мотоцикл с типом двигателя: {self.engine_type}")


bmw = Car("BMW", 2020, "X5", 4)
bmw.info()

yamaha = Motorcycle("Yamaha", 2018, "двухтактный")
yamaha.info()
