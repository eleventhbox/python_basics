revenue = float(input('Enter your revenue: '))
expenses = float(input('Enter your expenses: '))
fin_res = revenue - expenses
if fin_res > 0:
    print('Your profit is: {:.2f}'.format(abs(fin_res)))
    print('Your profitability: {:.2f}'.format(fin_res / revenue))
    number_of_employees = int(input('Enter number of employees: '))
    if number_of_employees > 0:
        print('Profit per employee: {:.2f}'.format(fin_res / number_of_employees))
else:
    print('Your loss is: {:.2f}'.format(abs(fin_res)))
