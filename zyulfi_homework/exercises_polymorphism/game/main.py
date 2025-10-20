from warrior import Warrior
from mage import Mage
from archer import Archer

chars = [Warrior(), Mage(), Archer()]
for c in chars:
    print(c.attack())