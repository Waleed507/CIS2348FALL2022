#Waleed Yusuf
#2104654

lj = int(input('Enter amount of lemon juice (in cups):\n'))
water = int(input('Enter amount of water (in cups):\n'))
an = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lj), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(an), 'cup(s) agave nectar')

ds = int(input('\nHow many servings would you like to make?\n'))
print('\nLemonade ingredients - yields', '{:.2f}'.format(ds), 'servings')
lj = lj*(ds/servings)
water = water*(ds/servings)
an = an*(ds/servings)
print('{:.2f}'.format(lj), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(an), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', '{:.2f}'.format(ds), 'servings')
print('{:.2f}'.format(16/lj), 'gallon(s) lemon juice')
print('{:.2f}'.format(water/16), 'gallon(s) water')
print('{:.2f}'.format(an/16), 'gallon(s) agave nectar')