# История:
# Сервиз пази данни за ремонтирани коли.
# Да се върне брой ремонти и кои са по-стари от 5 години.
# Очакван изход: ({'VW':2,'BMW':0}, ['VW'])
def car_service(cars):
    repairs_count = {}
    old_cars = []

    for brand, data in cars.items():
        # data = {'години': ..., 'ремонти': [...]}
        repairs_count[brand] = len(data['ремонти'])

        if data['години'] > 5:
            old_cars.append(brand)

    return repairs_count, old_cars


# --- Пример за използване ---
cars = {
    'VW': {'години': 7, 'ремонти': ['спирачки', 'масло']},
    'BMW': {'години': 3, 'ремонти': []}
}

print(car_service(cars))

