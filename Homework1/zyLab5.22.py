# Waleed Yusuf
# 2104654

oil = 35
tire_rot = 19
car_wash = 7
car_wax = 12
s1 = 0
s2 = 0
print('Davy\'s auto shop services')
print(f"Oil change -- ${oil}")
print(f"Tire rotation -- ${tire_rot}")
print(f"Car wash -- ${car_wash}")
print(f"Car wax -- ${car_wax}\n")

service1 = str(input('Select first service:\n'))
service2 = str(input('Select second service:\n'))

print('\nDavy\'s auto shop invoice\n')

if service1 == 'Oil change':
    s1 = oil
elif service1 == 'Tire rotation':
    s1 = tire_rot
elif service1 == 'Car wash':
    s1 = car_wash
elif service1 == 'Car wax':
    s1 = car_wax

if service2 == 'Oil change':
    s2 = oil
elif service2 == 'Tire rotation':
    s2 = tire_rot
elif service2 == 'Car wash':
    s2 = car_wash
elif service2 == 'Car wax':
    s2 = car_wax
elif service2 == '-':
    s2 = 0

if service1 == '-':
    print('Service 1: No service')
else:
    print(f"Service 1: {service1}, ${s1}")
if service2 == '-':
    print('Service 2: No service\n')
else:
    print(f"Service 2: {service2}, ${s2}\n")

total = s1 + s2
print(f"Total: ${total}")
