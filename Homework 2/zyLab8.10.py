# Waleed Yusuf
# 2104654

def palindrome(user_input):
    return user_input == user_input[::-1]


enter_input = input()
ans = enter_input
enter_input = enter_input.replace(' ', '')
output = palindrome(enter_input)

if output:
    print(f'{ans} is a palindrome')
else:
    print(f'{ans} is not a palindrome')
