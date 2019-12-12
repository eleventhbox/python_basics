# with *
def my_func1(num, exponent):
    num_tmp = 1
    exp_tmp = exponent
    while exp_tmp < 0:
        num_tmp *= abs(num)
        exp_tmp = exp_tmp + 1
    return 1 / num_tmp


print(f"""Result: {my_func1(float(input("Enter a number (positive): ")),
                            int(input("Enter a number's exponent (negative integer): ")))}""")


# without *
def my_func2(num, exponent):
    def mult(n_tmp, n):
        if n != 0:
            return n_tmp + mult(n_tmp, n - 1)
        else:
            return 0
    num_tmp = 1
    exp_tmp = exponent
    while exp_tmp < 0:
        num_tmp = mult(num_tmp, abs(num))
        exp_tmp = exp_tmp + 1
    return 1 / num_tmp


print(f"""Result: {my_func2(float(input("Enter a number (positive): ")),
                            int(input("Enter a number's exponent (negative integer): ")))}""")
