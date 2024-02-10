rows = int(input())
racing_number = input()
matrix = [input().split() for _ in range(rows)]
command = input()
total_kilometers_passed = 0
car_r = 0
car_c = 0
finished = False

while command != 'End' and not finished:
    if command == 'up':
        if car_r - 1 >= 0:
            car_r -= 1
    elif command == 'down':
        if car_r + 1 < rows:
            car_r += 1
    elif command == 'left':
        if car_c - 1 >= 0:
            car_c -= 1
    elif command == 'right':
        if car_c + 1 < rows:
            car_c += 1

    if matrix[car_r][car_c] == 'T':
        matrix[car_r][car_c] = '.'
        for row in range(rows):
            for col in range(rows):
                if matrix[row][col] == 'T':
                    car_r = row
                    car_c = col
                    matrix[car_r][car_c] = '.'
        total_kilometers_passed += 30
    elif matrix[car_r][car_c] == 'F':
        total_kilometers_passed += 10
        finished = True
    else:
        total_kilometers_passed += 10
        matrix[car_r][car_c] = '.'
    command = input()
matrix[car_r][car_c] = 'C'


if finished:
    print(f'Racing car {racing_number} finished the stage!')
else:
    print(f'Racing car {racing_number} DNF.')
print(f'Distance covered {total_kilometers_passed} km.')
for row in matrix:
    print(''.join(row))
