from animal import Animal
from zookeeper import Zookeeper
from zoo import Zoo

a1 = Animal("Lion", 5)
a2 = Animal("Elephant", 12)
zk = Zookeeper("Peter")

zk.add_animal(a1)
zk.add_animal(a2)

z = Zoo()
z.add_keeper(zk)

print(z.all_animals())  # ['Lion', 'Elephant']