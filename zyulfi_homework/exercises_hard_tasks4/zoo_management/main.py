from animal import Animal
from cage import Cage
from zoo import Zoo

a1 = Animal("Kotka", "ris")
a2 = Animal("kotka2", "lion")
c1 = Cage(123, 2)
c2 = Cage(236, 5)
c1.add_animal(a1)
c1.add_animal(a2)
c2.add_animal(a1)
z = Zoo()
z.add_cage(c1)
z.add_cage(c2)
print(z.total_animals())
print(z.largest_cage().number)
