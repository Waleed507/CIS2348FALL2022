# Waleed Yusuf
# 2104654

numbers = input()
temp_list = numbers.split()

num_list = []

for i in temp_list:
    temp = int(i)
    if temp >= 0:
        num_list.append(temp)

num_list.sort()

for integers in num_list:
    print(integers, end=" ")
