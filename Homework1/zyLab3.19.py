#Waleed Yusuf
#2104654

dict = {
    "red": 35,
    "blue": 25,
    "green": 23
}

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
wall_area = height*width
print('Wall area:', wall_area, 'square feet')

gallon = 350
paint_req = wall_area/gallon
print('Paint needed:', '{:.2f}'.format(paint_req), 'gallons')
print('Cans needed:', round(paint_req), 'can(s)\n')
choice = input('Choose a color to paint the wall:\n')
print(f'Cost of purchasing {choice} paint: ${dict[choice]*round(paint_req)}')