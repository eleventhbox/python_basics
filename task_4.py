# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
word_map = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
src = open("text_4_src.txt", "r", encoding="utf-8")
tgt = open("text_4_tgt.txt", "w", encoding="utf-8")
for line in src:
    lst_tmp = line.split(' ')
    tgt.write(word_map[lst_tmp[0]] + ' ' + lst_tmp[1] + ' ' + lst_tmp[2])
src.close()
tgt.close()
