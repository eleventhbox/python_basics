# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce

f = open("text_3.txt", "r", encoding="utf-8")
lst = []
emp_lst = []
for i in f:
    lst_tmp = i.split(' ')
    lst.append(int(lst_tmp[1]))
    if int(lst_tmp[1]) < 20000:
        emp_lst.append(lst_tmp[0])
avg = reduce(lambda a, b: a + b, lst) / len(lst)
print(f'List of employees whose salary is less than 20000 \u20bd: {", ".join(emp_lst)}')
print(f'Average salary is: {round(avg, 2)}')
f.close()
