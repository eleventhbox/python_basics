lst = (input("Enter a sentence of more than one word separated by single spaces: ")).split(' ')
for idx, word in enumerate(lst):
    print(f'Row number: {idx+1}, word: {word[0:10]}')
