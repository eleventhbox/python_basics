a = abs(int(input('Enter positive integer a: ')))
b = abs(int(input('Enter positive integer b: ')))
nth_day = 1
while b > a:
    a = a * 1.1
    nth_day += 1
print(f'Number of day: {nth_day}')
