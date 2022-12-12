# Waleed Yusuf
# 2104654

import csv
from datetime import datetime

# Read the ManufacturerList.csv file and store the data in a list
with open('ManufacturerList.csv', 'r') as manufacturer_list:
    manufacturer_list_reader = csv.reader(manufacturer_list)
    manufacturer_list_data = list(manufacturer_list_reader)

# Read the PriceList.csv file and store the data in a list
with open('PriceList.csv', 'r') as price_list:
    price_list_reader = csv.reader(price_list)
    price_list_data = list(price_list_reader)

# Read the ServiceDatesList.csv file and store the data in a list
with open('ServiceDatesList.csv', 'r') as service_dates_list:
    service_dates_list_reader = csv.reader(service_dates_list)
    service_dates_list_data = list(service_dates_list_reader)


while True:
    # Get the user input
    user_input = input("Please enter the manufacturer and item type: ")
    # If the user enters 'q' then exit the program
    if user_input == 'q':
        break
    # Split the user input into a list
    user_input_list = user_input.split()
    # Check if the user input contains more than 2 words
    if len(user_input_list) < 2:
        print("No such item in inventory")
        continue

    manufacturerMatched = False
    manufacturerMatchedIndex = -1
    itemTypeMatched = False
    itemTypeMatchedIndex = -1

    # Check if the manufacturer and item type are in the inventory
    for i in range(len(manufacturer_list_data)):
        if manufacturer_list_data[i][1].lower() in user_input.lower():
            manufacturerMatched = True
            manufacturerMatchedIndex = i
        if manufacturer_list_data[i][2].lower() in user_input.lower():
            itemTypeMatched = True
            itemTypeMatchedIndex = i
        if manufacturerMatched and itemTypeMatched and manufacturerMatchedIndex == itemTypeMatchedIndex:
            break

    # print(manufacturerMatched, itemTypeMatched,
    #       manufacturerMatchedIndex, itemTypeMatchedIndex)

    # If the manufacturer and item type are not in the inventory, print the message
    if not manufacturerMatched or not itemTypeMatched:
        print("No such item in inventory")
        continue

    # If the manufacturer and item type are in the inventory, check if the combination is in the inventory
    if manufacturerMatchedIndex != itemTypeMatchedIndex:
        print("No such item in inventory")
        continue

    valid_item = True
    # If the combination is in the inventory, check if the item is damaged or past its service date
    for i in range(len(manufacturer_list_data)):
        if manufacturer_list_data[i][0] == manufacturer_list_data[manufacturerMatchedIndex][0]:
            if manufacturer_list_data[i][3] == 'damaged':
                print("No such item in inventory")
                valid_item = False

    if not valid_item:
        continue

    valid_item = True
    for i in range(len(service_dates_list_data)):
        if service_dates_list_data[i][0] == manufacturer_list_data[manufacturerMatchedIndex][0]:
            if datetime.strptime(service_dates_list_data[i][1], '%m/%d/%Y') < datetime.now():
                print("No such item in inventory")
                valid_item = False

    if not valid_item:
        continue

    # If the combination is in the inventory and the item is not damaged or past its service date, print the item details
    for i in range(len(manufacturer_list_data)):
        if manufacturer_list_data[i][0] == manufacturer_list_data[manufacturerMatchedIndex][0]:
            print("Your item is: ", end='')
            print(manufacturer_list_data[i][0], manufacturer_list_data[i]
                  [1], manufacturer_list_data[i][2], end=' ')
            # find the highest price of the item
            highest_price = 0
            for j in range(len(price_list_data)):
                if price_list_data[j][0] == manufacturer_list_data[i][0]:
                    if float(price_list_data[j][1]) > highest_price:
                        highest_price = float(price_list_data[j][1])
            print(f'price: ${highest_price}')

    # If the combination is in the inventory and the item is not damaged or past its service date, print the item details of the same item type from another manufacturer that closes in price to the output item
    similarItemIndex = -1
    for i in range(len(manufacturer_list_data)):
        if manufacturer_list_data[i][0] != manufacturer_list_data[manufacturerMatchedIndex][0] and manufacturer_list_data[i][2] == manufacturer_list_data[manufacturerMatchedIndex][2]:
            similarItemIndex = i
            break

    if similarItemIndex != -1:
        valid_item = True
        # If the combination is in the inventory, check if the item is damaged or past its service date
        for i in range(len(manufacturer_list_data)):
            if manufacturer_list_data[i][0] == manufacturer_list_data[similarItemIndex][0]:
                if manufacturer_list_data[i][3] == 'damaged':
                    valid_item = False

        if not valid_item:
            continue

        valid_item = True
        for i in range(len(service_dates_list_data)):
            if service_dates_list_data[i][0] == manufacturer_list_data[similarItemIndex][0]:
                if datetime.strptime(service_dates_list_data[i][1], '%m/%d/%Y') < datetime.now():
                    valid_item = False

        if not valid_item:
            continue
        print("You may also, consider: ", end='')
        print(manufacturer_list_data[similarItemIndex][0], manufacturer_list_data[similarItemIndex]
              [1], manufacturer_list_data[similarItemIndex][2], end=' ')
        # find the highest price of the item
        highest_price = 0
        for j in range(len(price_list_data)):
            if price_list_data[j][0] == manufacturer_list_data[similarItemIndex][0]:
                if float(price_list_data[j][1]) > highest_price:
                    highest_price = float(price_list_data[j][1])
        print(f'price: ${highest_price}')
