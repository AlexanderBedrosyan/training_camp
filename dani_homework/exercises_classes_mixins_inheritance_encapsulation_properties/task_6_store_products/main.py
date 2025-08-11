from perishable import Perishable
from electronics import Electronics

milk = Perishable("Milk", 2.5, "01-08-2025")
#print(milk.is_expired("09-08-2025"))  # True
print(milk.is_expired())  # True

tv = Electronics("TV", 500, 24)
print(tv.is_under_warranty(18))  # True