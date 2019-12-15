def gen_dict(lst):
    for k, v in {el: lst.count(el) for el in lst}.items():
        if v == 1:
            yield k


lst = [7, 1, 1, 3, 4, 2, 4, 5, 6, 2]
print(' '.join(map(str, [el for el in gen_dict(lst)])))
