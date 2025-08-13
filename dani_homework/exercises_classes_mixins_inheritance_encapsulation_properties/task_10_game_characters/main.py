from warrior import Warrior
from mage import Mage

w = Warrior("Thor", 100)
w.attack()

m = Mage("Gandalf", 80, 100)
m.cast_spell("Fireball")
print(m.mana)