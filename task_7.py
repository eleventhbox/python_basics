from itertools import count
from math import factorial


def fibo_gen():
    for el in count():
        yield factorial(el)


for idx, el in enumerate(fibo_gen()):
    if idx <= 15:
        print(el)
