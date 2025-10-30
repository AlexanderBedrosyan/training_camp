from dog import Dog
from cat import Cat
from cow import Cow

animals = [Dog(), Cat(), Cow()]
for a in animals:
    print(a.make_sound())