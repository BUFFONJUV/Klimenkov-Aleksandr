# Чтение данных из файла и создание нового файла с машинами с пробегом меньше 10000
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
count = 0
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
    if odometer < 10000 and color == 'серебро' and count < 5:
        print(f'{manufacturer} {model} есть машина серебряного цвета. Ее стоимость {price} и пробег: {odometer}')
        count += 1
