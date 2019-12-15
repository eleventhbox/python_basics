import itertools

in_str = input("Enter the start number: ")
for el in itertools.count(0 if in_str == '' else int(in_str)):
    print(el)


lst = [1, 2, 3, 4, 5]
for el in itertools.cycle(lst):
    print(el)