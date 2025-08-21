# Клас Machine с класов атрибут machines_created,
# който се увеличава при всяка нова машина

class Machine:
    machines_created = 0

    def __init__(self):
        Machine.machines_created += 1