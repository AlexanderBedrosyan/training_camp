from percentage_discount import PercentageDiscount
from fixed_discount import FixedDiscount
from no_discount import NoDiscount

discounts = [PercentageDiscount(10), FixedDiscount(5), NoDiscount()]
for d in discounts:
    print(d.apply(100))
