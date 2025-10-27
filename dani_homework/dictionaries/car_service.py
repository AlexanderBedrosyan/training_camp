# История: Сервиз пази данни за ремонтирани коли.
# Да се върне брой ремонти и кои са по-стари от 5 години.
# from datetime import datetime def service_report(cars): year = datetime.now().year repairs = {c["модел"]: len(c["ремонти"]) for c in cars} old_cars = [c["модел"] for c in cars if year - c["година"] > 5] return repairs, old_cars
# cars = [ {"модел":"VW","година":2015,"ремонти":["масло","гуми"]},
# {"модел":"BMW","година":2022,"ремонти":[]} ]
# print(service_report(cars))
# Очакван изход: ({'VW':2,'BMW':0}, ['VW'])

cars = [
    {"модел":"VW", "година":2015, "ремонти":["масло","гуми"]},
    {"модел":"BMW", "година":2022, "ремонти":[]}
]
print(service_report(cars))