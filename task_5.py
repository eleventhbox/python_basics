lst = [7, 5, 3, 3, 2]
while True:
    in_str = input("Enter a new rating integer or ! to stop :")
    if in_str == '!':
        break
    lst_tmp = lst[:]
    lst_tmp.extend([int(in_str)])
    print(sorted(lst_tmp, reverse=True))
