# Създай клас Car, който има атрибути brand и year. Добави метод, който принтира колко години е колата.
from datetime import date

class Car:

    def __init__(self, brand=str, year=int):
        self.brand = brand
        self.year = year

    def current_year(self):
        current_date = date.today()
        return current_date.year

    def is_valid_year(self):
        return self.year <= self.current_year()

    def car_years_old(self):
        # current_date = date.today()
        # current_year = current_date.year

        if not self.is_valid_year():
            return "Insert a wrong year for the car and needs correction"
        car_years_old = self.current_year() - self.year
        return car_years_old


car = Car("trabant", 2030)
print(car.car_years_old())
print(car.is_valid_year())

car.year = 2020
print(car.car_years_old())