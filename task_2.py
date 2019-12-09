lst = input("Enter a comma separated list of values: ").replace(' ', '').split(',')
for i in range(0, len(lst), 2):
    try:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    except IndexError:
        print(i)
        pass
print(str(lst))
