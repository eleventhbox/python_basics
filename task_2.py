number_of_sec = int(input('Enter a number of seconds as an integer in the range from 0 to 359999: '))
number_of_hh = number_of_sec // 3600
number_of_ss_remain = number_of_sec % 3600
number_of_mi = number_of_ss_remain // 60
number_of_ss = number_of_ss_remain % 60
print('{0:0=2}:{1:0=2}:{2:0=2}'.format(number_of_hh, number_of_mi, number_of_ss))
