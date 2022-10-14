# Waleed Yusuf
# 2104654

from datetime import date


# Function to convert months in string into integer
def get_month_int(month_string):

    if month_string == 'January':
        month_int = 1
    elif month_string == 'February':
        month_int = 2
    elif month_string == 'March':
        month_int = 3
    elif month_string == 'April':
        month_int = 4
    elif month_string == 'May':
        month_int = 5
    elif month_string == 'June':
        month_int = 6
    elif month_string == 'July':
        month_int = 7
    elif month_string == 'August':
        month_int = 8
    elif month_string == 'September':
        month_int = 9
    elif month_string == 'October':
        month_int = 10
    elif month_string == 'November':
        month_int = 11
    elif month_string == 'December':
        month_int = 12
    else:
        month_int = 0
    return str(month_int)


# initializing lists and string variables
today = date
month = []
day = []
year = []
date_list = []
temp_month = ''
temp_string = ''
user_string = input()
while user_string != '-1':  # Loop until user enters -1
    temp_month = get_month_int(user_string.split()[0])
    # Condition to make sure input is in the correct format
    if temp_month != '0' and user_string.find(",") != -1 and user_string.find(", ") != -1:
        month = temp_month
        temp_string += month
        day = user_string.split()[1]  # Gets the day from input
        day = day.replace(",", "")
        temp_string += '/'
        temp_string += day
        year = user_string.split()[2]  # Gets the year from input
        temp_string += '/'
        temp_string += year
    else:
        pass
    d1 = date(int(year), int(month), int(day))
    d2 = date.today()
    if d1 > d2:  # Comparing input date with current date
        temp_string = ''

    date_list.append(temp_string)  # Adding to end of the list
    temp_string = ''
    user_string = input()
for item in date_list:  # Loop to filter the desired output
    if item in date_list == " ":
        date_list.remove(" ")
    print(item)
