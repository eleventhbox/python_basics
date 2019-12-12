acc_sum = 0
while True:
    in_str = input("Enter a space separated string of numbers or ! to exit: ")
    lst = in_str.split(sep=' ')
    try:
        acc_sum += sum(map(int, lst[0:lst.index("!")] if '!' in lst else lst))
        print(f'Result: {acc_sum}')
        if '!' in lst:
            break
    except ValueError:
        print('Only numbers are expected or ! symbol')