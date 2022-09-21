# Waleed Yusuf
# 2104654

print('Birthday Calculator')
print('Current day')

# Takes input for current date
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_yr = int(input('Year: '))

print('Birthday')

# Takes input for birth date
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_yr = int(input('Year: '))

# Subtracts current year and birth year, compares the month and day
# If current month and day is less than birth month and day then it subtracts 1 from the age
age = current_yr - birth_yr - ((current_month, current_day) < (birth_month, birth_day))

print('You are', age, 'years old.')
