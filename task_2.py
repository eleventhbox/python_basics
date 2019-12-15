def gen_new_list(lst):
    tmp = 0
    for idx, el in enumerate(lst):
        if idx == 0:
            tmp = el
        else:
            if el > tmp:
                tmp = el
                yield el


print([el for el in gen_new_list([1, 3, 2, 6, 4, 2, 7])])
