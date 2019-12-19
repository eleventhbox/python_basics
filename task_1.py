# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
f = open("text_1.txt", "w")
print("Enter multiple lines to add to a text file. To save the file enter an empty line => ", end="")
str_lst = []
while True:
    in_str = input()
    if in_str == '':
        break
    else:
        str_lst.append(in_str + '\n')
if len(str_lst) > 0:
    str_lst[-1] = str_lst[-1].rstrip('\n')
f.writelines(str_lst)
f.close()
