def my_func(arg1, arg2, arg3):
    return sum(sorted((arg1, arg2, arg3), reverse=True)[0:2])


print(f'Result = {my_func(float(input("Enter arg1: ")), float(input("Enter arg2: ")), float(input("Enter arg3: "))):.2f}')
