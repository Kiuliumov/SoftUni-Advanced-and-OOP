n = int(input())


def is_valid(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


matrix = [list(input()) for _ in range(n)]
ship_r, ship_c = None, None
enough = False
value = 0
for i in range(n):
    current_row = matrix[i]
    if 'S' in current_row:
        ship_r = i
        ship_c = current_row.index('S')
command = input()
while command != 'collect the nets':
    ship_last_r, ship_last_c = ship_r, ship_c
    if command == 'up':
        if is_valid(ship_r - 1, ship_c):
            ship_r -= 1
        else:
            ship_r = n - 1
    elif command == 'down':
        if is_valid(ship_r + 1, ship_c):
            ship_r += 1
        else:
            ship_r = 0
    elif command == 'left':
        if is_valid(ship_r, ship_c - 1):
            ship_c -= 1
        else:
            ship_c = n - 1
    elif command == 'right':
        if is_valid(ship_r, ship_c + 1):
            ship_c += 1
        else:
            ship_c = 0
    if matrix[ship_r][ship_c] == 'W':
        last_coordinates = f'[{ship_r},{ship_c}]'
        print(f'You fell into a whirlpool! The ship sank and you lost the you caught. Last coordinates of the '
              f'ship: {last_coordinates}')
        break
    elif matrix[ship_r][ship_c].isdigit():
        value += int(matrix[ship_r][ship_c])
        if value >= 20 and not enough:
            print(f'Success! You managed to reach the quota!')
            enough = True
    matrix[ship_last_r][ship_last_c] = '-'
    matrix[ship_r][ship_c] = 'S'
    command = input()
else:
    if not enough:
        print(f"You didn't catch enough and didn't reach the quota! You need {20 - value} tons of fish more.")
    for row in matrix:
        print(''.join(row))

