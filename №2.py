with open('cars.txt', 'r', encoding='utf-8') as file:
    cars = file.readlines()

with open('odometer_car.txt', 'w', encoding='utf-8') as file:
    for car in cars[1:]:
        car_info = car.strip().split('$')
        manufacturer = car_info[2]
        model = car_info[3]
        color = car_info[5]
        if '.' in car_info[4]:
            odometer = float(car_info[4])
        else:
            odometer = int(car_info[4])
        price = int(car_info[0])
        if odometer < 10000.0:
            file.write(f'{manufacturer} {model}; Цвет: {color}; Пробег: {odometer}; Цена: {price}\n')

# Вывод пяти машин с пробегом меньше 10000 и цветом "серебро"
n = 0
k = 0
l = 0
m = 0
f = 0
for car in cars[1:]:
    car_info = car.strip().split('$')
    manufacturer = car_info[2]
    model = car_info[3]
    color = car_info[5]
    if '.' in car_info[4]:
        odometer = float(car_info[4])
    else:
        odometer = int(car_info[4])
    price = int(car_info[0])
    price = int(car_info[0])
    if color=='красный':
        n+= 1
    if color=='черный':
        k+= 1
    if color=='серебро':
        l+= 1
    if color=='белый':
        m+= 1
    if color=='желтый':
        f+= 1
print( '=n' 'машин цвета красный есть сегодня в наличии.')
print( '=k' 'машин цвета черный есть сегодня в наличии.')
print( '=l' 'машин цвета серебро есть сегодня в наличии.')