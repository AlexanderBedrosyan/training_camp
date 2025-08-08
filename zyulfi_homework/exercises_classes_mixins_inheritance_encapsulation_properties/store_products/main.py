from perishable import Perishable
from electronics import Electronics

milk = Perishable("Milk", 2.5, "2025-08-01")
print(milk.is_expired("2025-08-09"))  # True

tv = Electronics("TV", 500, 24)
print(tv.is_under_warranty(18))  # True