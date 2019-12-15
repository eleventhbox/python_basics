from operator import mul
from functools import reduce

print(reduce(mul, [el for el in range(100, 1001, 2)]))
