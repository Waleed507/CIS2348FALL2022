# Waleed Yusuf
# 2104654

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print(name, age)
        parts = input().split()
        name = parts[0]

    except ValueError as error:
        age = 0
        print(name, age)
        parts = input().split()
        name = parts[0]
