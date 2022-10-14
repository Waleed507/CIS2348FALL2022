# Waleed Yusuf
# 2104654

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

solution = False
val1 = 0
val2 = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        if (a1*x)+(b1*y) == c1 and (a2*x)+(b2*y) == c2:
            solution = True
            val1 = x
            val2 = y

if solution:
    print(val1, val2)
else:
    print('No solution')
