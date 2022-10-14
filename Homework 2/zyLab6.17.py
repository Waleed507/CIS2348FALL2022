# Waleed Yusuf
# 2104654

password = input()

for character in password:
    if character == 'i':
        password = password.replace('i', '!')

    elif character == 'a':
        password = password.replace('a', '@')

    elif character == 'm':
        password = password.replace('m', 'M')

    elif character == 'B':
        password = password.replace('B', '8')

    elif character == 'o':
        password = password.replace('o', '.')

else:
    password += 'q*s'

print(password)
