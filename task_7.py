# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
from functools import reduce
import json

with open("text_7_src.txt", "r", encoding="utf-8") as src:
    f_lst = list(src)
    avg_profit = 0
    lst_tmp = [
        i for i in [
            (float(i.split(' ')[2]) - float(i.split(' ')[3]))
            for i in f_lst
        ] if i > 0
    ]
    if len(lst_tmp) > 0:
        avg_profit = round(float(reduce(lambda a, b: a + b, lst_tmp)) / len(lst_tmp), 2)
    res_lst = []
    frm_dict = {}
    for line in f_lst:
        lst_tmp = line.split(' ')
        frm_dict[lst_tmp[0]] = float(lst_tmp[2]) - float(lst_tmp[3])
    res_lst.append(frm_dict)
    res_lst.append({"average_profit": avg_profit})
with open('text_7_tgt.json', 'w') as tgt:
    json.dump(res_lst, tgt)
