class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped.")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging.")


class GasolineCar(Car):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"{self.brand} {self.model} is refueling.")


# Створення екземплярів класів
electric_car = ElectricCar("Tesla", "Model S", 2023, "100 kWh")
gasoline_car = GasolineCar("Toyota", "Corolla", 2023, "Petrol")

# Виклики методів
electric_car.start_engine()
electric_car.charge()
electric_car.stop_engine()

print()

gasoline_car.start_engine()
gasoline_car.refuel()
gasoline_car.stop_engine()