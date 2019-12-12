def print_user_data(first_name, last_name, year_of_birth, city, email, phone):
    print(f'First name: {first_name}, last name: {last_name}, year_of_birth: {year_of_birth}, '
          f'city: {city}, email: {email}, phone: {phone}')


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
year_of_birth = input("Enter year of birth: ")
city = input("Enter city: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
print_user_data(first_name=first_name, last_name=last_name, year_of_birth=year_of_birth, city=city, email=email, phone=phone)
