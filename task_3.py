lst = ["winter", "winter",
       "spring", "spring", "spring",
       "summer", "summer", "summer",
       "autumn", "autumn", "autumn",
       "winter"]
num_of_month = int(input("Enter a number of the month: "))
print(f"A season of the chosen month is: {lst[num_of_month-1]}")

dct = {1: "winter", 2: "winter",
       3: "spring", 4: "spring", 5: "spring",
       6: "summer", 7: "summer", 8: "summer",
       9: "autumn", 10: "autumn", 11: "autumn",
       12: "winter"}

num_of_month = int(input("Enter a number of the month: "))
print(f"A season of the chosen month is: {dct[num_of_month]}")
