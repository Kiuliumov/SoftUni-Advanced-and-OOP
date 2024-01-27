n = int(input())
cars = []
for _ in range(n):
    command,number = input().split(' ')
    if command == 'IN,':
        cars.append(number)
    elif command == 'OUT,':
        cars.remove(number)
if cars:
    cars = set(cars)
    for car in cars:
        print(car)
else:
    print(f'Parking Lot is Empty')