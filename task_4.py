random_integer = abs(int(input('Enter a random positive integer: ')))
max_digit = 0
max_digit_tmp = 0
while True:
    if random_integer >= 0 and random_integer < 10:
        if random_integer > max_digit:
            max_digit = random_integer
        break
    else:
        max_digit_tmp = random_integer % 10
        if max_digit_tmp > max_digit:
            max_digit = max_digit_tmp
        random_integer = random_integer // 10
print(max_digit)
