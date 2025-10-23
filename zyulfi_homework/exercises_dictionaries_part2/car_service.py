# ЗАДАЧА 9: Сервиз за автомобили
# История:
# Сервиз пази данни за ремонтирани коли.
# Да се върне брой ремонти и кои са по-стари от 5 години.
# cars = [ {"модел":"VW","година":2015,"ремонти":["масло","гуми"]}, {"модел":"BMW","година":2022,"ремонти":[]} ] print(service_report(cars))
#
# Очакван изход: ({'VW':2,'BMW':0}, ['VW'])

class CarService:
    def __init__(self, curr_cars):
        self.curr_cars = curr_cars

    def repairs_car(self):
        cars_dict = {}
        list_of_old_cars = []
        for element in self.curr_cars:
            model = element["модел"]
            year = element["година"]
            repairs = element["ремонти"]

            count_of_repairs = len(repairs)
            if (2025 - year) > 5:
                list_of_old_cars.append(model)

            cars_dict[model] = count_of_repairs

        return cars_dict, list_of_old_cars


cars = [ {"модел":"VW","година":2015,"ремонти":["масло","гуми"]}, {"модел":"BMW","година":2022,"ремонти":[]} ]

cars = CarService(cars)
print(cars.repairs_car())

# print(service_report(cars))

# Очакван изход: ({'VW':2,'BMW':0}, ['VW'])