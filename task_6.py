def my_func1(s):
    print(s.title())


my_func1(input("Enter a word: "))


def my_func2(s):
    print(' '.join(map(str.title, s.split(sep=' '))))


my_func2(input("Enter a string of space separated words: "))
