lst_names = input("Enter a comma separated list of items: ").split(',')
lst_prices = input("Enter a comma separated list of prices: ").split(',')
lst_amounts = input("Enter a comma separated list of amounts: ").split(',')
str_uom = input("Enter a unit of measure: ")

if len(lst_names) != len(lst_prices) != len(lst_amounts):
    raise Exception("Number of elements in lists should be equal")

lst_num = list(range(1, len(lst_names) + 1))
lst_uom = [str_uom] * len(lst_names)

res_lst = []
for i in list(zip(lst_num, lst_prices, lst_amounts, lst_uom)):
    res_lst.append(
        (i[0], {"название": i[1], "цена": i[1], "количество": i[2], "ед": i[3]})
    )
print(res_lst)
