# Waleed Yusuf
# 2104654

import csv
from datetime import datetime


def bubble_sort(data, by=None, reverse=False):
    if by is None:
        by = []
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if reverse:
                if data[j][by[0]] < data[j + 1][by[0]]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                elif data[j][by[0]] == data[j + 1][by[0]]:
                    if len(by) > 1:
                        if data[j][by[1]] < data[j + 1][by[1]]:
                            data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][by[0]] > data[j + 1][by[0]]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                elif data[j][by[0]] == data[j + 1][by[0]]:
                    if len(by) > 1:
                        if data[j][by[1]] < data[j + 1][by[1]]:
                            data[j], data[j + 1] = data[j + 1], data[j]

    return data


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


# Create a list of lists to store the data for FullInventory.csv
full_inventory_data = []

# Iterate through the manufacturer_list_data list
for manufacturer_list_row in manufacturer_list_data:
    # Iterate through the price_list_data list
    for price_list_row in price_list_data:
        # Iterate through the service_dates_list_data list
        for service_dates_list_row in service_dates_list_data:
            # Check if the item ID in the manufacturer_list_row is the same as the item ID in the price_list_row
            if manufacturer_list_row[0] == price_list_row[0]:
                # Check if the item ID in the manufacturer_list_row is the same as the item ID in the service_dates_list
                if manufacturer_list_row[0] == service_dates_list_row[0]:
                    # Create a list to store the data for the current row
                    current_row = [manufacturer_list_row[0], manufacturer_list_row[1], manufacturer_list_row[2],
                                   price_list_row[1], service_dates_list_row[1], manufacturer_list_row[3]]
                    # Add the current_row list to the full_inventory_data list
                    full_inventory_data.append(current_row)


# Sort the full_inventory_data list by the manufacturer name and item type if the manufacturer name is the same
full_inventory_data = bubble_sort(
    full_inventory_data, by=[1], reverse=False)


# Write the full_inventory_data list to the FullInventory.csv file
with open('FullInventory.csv', 'w', newline='') as full_inventory:
    full_inventory_writer = csv.writer(full_inventory)
    for row in full_inventory_data:
        full_inventory_writer.writerow(row)


# Create a list of lists to store the data for LaptopInventory.csv
laptop_inventory_data = []
phone_inventory_data = []
tower_inventory_data = []

# Iterate through the manufacturer_list_data list
for manufacturer_list_row in manufacturer_list_data:
    # Iterate through the price_list_data list
    for price_list_row in price_list_data:
        # Iterate through the service_dates_list_data list
        for service_dates_list_row in service_dates_list_data:
            # Check if the item ID in the manufacturer_list_row is the same as the item ID in the price_list_row
            if manufacturer_list_row[0] == price_list_row[0]:
                # Check if the item ID in the manufacturer_list_row is the same as the item ID in the service_dates_list
                if manufacturer_list_row[0] == service_dates_list_row[0]:
                    # Check if the item type in the manufacturer_list_row is a laptop
                    if manufacturer_list_row[2] == 'laptop':
                        # Create a list to store the data for the current row
                        current_row = [manufacturer_list_row[0], manufacturer_list_row[1], price_list_row[1],
                                       service_dates_list_row[1], manufacturer_list_row[3]]
                        # Add the current_row list to the laptop_inventory_data list
                        laptop_inventory_data.append(current_row)
                    elif manufacturer_list_row[2] == 'phone':
                        # Create a list to store the data for the current row
                        current_row = [manufacturer_list_row[0], manufacturer_list_row[1], price_list_row[1],
                                       service_dates_list_row[1], manufacturer_list_row[3]]
                        # Add the current_row list to the phone_inventory_data list
                        phone_inventory_data.append(current_row)
                    elif manufacturer_list_row[2] == 'tower':
                        # Create a list to store the data for the current row
                        current_row = [manufacturer_list_row[0], manufacturer_list_row[1], price_list_row[1],
                                       service_dates_list_row[1], manufacturer_list_row[3]]
                        # Add the current_row list to the tower_inventory_data list
                        tower_inventory_data.append(current_row)

# Sort the laptop_inventory_data list by item ID
laptop_inventory_data = bubble_sort(
    laptop_inventory_data, by=[0], reverse=False)
phone_inventory_data = bubble_sort(
    phone_inventory_data, by=[0], reverse=False)
tower_inventory_data = bubble_sort(
    tower_inventory_data, by=[0], reverse=False)

# Write the laptop_inventory_data list to the LaptopInventory.csv file
with open('LaptopInventory.csv', 'w', newline='') as laptop_inventory:
    laptop_inventory_writer = csv.writer(laptop_inventory)
    for row in laptop_inventory_data:
        laptop_inventory_writer.writerow(row)

with open('PhoneInventory.csv', 'w', newline='') as phone_inventory:
    phone_inventory_writer = csv.writer(phone_inventory)
    for row in phone_inventory_data:
        phone_inventory_writer.writerow(row)

with open('TowerInventory.csv', 'w', newline='') as tower_inventory:
    tower_inventory_writer = csv.writer(tower_inventory)
    for row in tower_inventory_data:
        tower_inventory_writer.writerow(row)


# Create a list of lists to store the data for PastServiceDateInventory.csv
past_service_date_inventory_data = []

# Iterate through the manufacturer_list_data list
for manufacturer_list_row in manufacturer_list_data:
    # Iterate through the price_list_data list
    for price_list_row in price_list_data:
        # Iterate through the service_dates_list_data list
        for service_dates_list_row in service_dates_list_data:
            # Check if the item ID in the manufacturer_list_row is the same as the item ID in the price_list_row
            if manufacturer_list_row[0] == price_list_row[0]:
                # Check if the item ID in the manufacturer_list_row is the same as the item ID in the service_dates_list
                if manufacturer_list_row[0] == service_dates_list_row[0]:
                    # Check if the service date in the service_dates_list_row is before today's date
                    if datetime.strptime(service_dates_list_row[1], '%m/%d/%Y') < datetime.now():
                        # Create a list to store the data for the current row
                        current_row = [manufacturer_list_row[0], manufacturer_list_row[1], manufacturer_list_row[2],
                                       price_list_row[1], service_dates_list_row[1], manufacturer_list_row[3]]
                        # Add the current_row list to the past_service_date_inventory_data list
                        past_service_date_inventory_data.append(current_row)

# Sort the past_service_date_inventory_data list by service date of the item from oldest to newest
past_service_date_inventory_data = bubble_sort(
    past_service_date_inventory_data, by=[4], reverse=False)

# Write the past_service_date_inventory_data list to the PastServiceDateInventory.csv file
with open('PastServiceDateInventory.csv', 'w', newline='') as past_service_date_inventory:
    past_service_date_inventory_writer = csv.writer(
        past_service_date_inventory)
    for row in past_service_date_inventory_data:
        past_service_date_inventory_writer.writerow(row)


# Create a list of lists to store the data for DamagedInventory.csv
damaged_inventory_data = []

# Iterate through the manufacturer_list_data list
for manufacturer_list_row in manufacturer_list_data:
    # Iterate through the price_list_data list
    for price_list_row in price_list_data:
        # Iterate through the service_dates_list_data list
        for service_dates_list_row in service_dates_list_data:
            # Check if the item ID in the manufacturer_list_row is the same as the item ID in the price_list_row
            if manufacturer_list_row[0] == price_list_row[0]:
                # Check if the item ID in the manufacturer_list_row is the same as the item ID in the service_dates_list
                if manufacturer_list_row[0] == service_dates_list_row[0]:
                    # check if the item is damaged
                    if manufacturer_list_row[3] == 'damaged':
                        # Create a list to store the data for the current row
                        current_row = [manufacturer_list_row[0], manufacturer_list_row[1], manufacturer_list_row[2],
                                       price_list_row[1], service_dates_list_row[1]]
                        # Add the current_row list to the damaged_inventory_data list
                        damaged_inventory_data.append(current_row)

# Sort the damaged_inventory_data list by price of the item from highest to lowest
damaged_inventory_data = bubble_sort(
    damaged_inventory_data, by=[3], reverse=True)

# Write the damaged_inventory_data list to the DamagedInventory.csv file
with open('DamagedInventory.csv', 'w', newline='') as damaged_inventory:
    damaged_inventory_writer = csv.writer(damaged_inventory)
    for row in damaged_inventory_data:
        damaged_inventory_writer.writerow(row)
