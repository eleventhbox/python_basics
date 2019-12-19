# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
line_num = sum(1 for line in open('text_2.txt'))
dct = {
    k + 1: len([el for el in lst.split(' ') if len(el) > 0])
    for (k, lst) in list(
        enumerate(open("text_2.txt"))
    )
}
print(f'Number of lines: {line_num}')
print(f'Number of words in every line: {dct}')
