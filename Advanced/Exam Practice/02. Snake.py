n = int(input())
matrix = [list(input()) for _ in range(n)]
snake_r, snake_c = None,None
food = 0
for row in matrix:
    if 'S' in row:
        snake_r = matrix.index(row)
        snake_c = row.index('S')
while food < 10:
    matrix[snake_r][snake_c] = '.'
    counter = 1
    command = input()
    if command == 'up':
        snake_r -= 1
    if command == 'down':
        snake_r += 1
    if command == 'left':
        snake_c -= 1
    if command == 'right':
        snake_c += 1
    if not 0 <= snake_r < n or not 0 <= snake_c < n:
        print('Game over!')
        break
    if matrix[snake_r][snake_c] == '*':
        food += 1
    if matrix[snake_r][snake_c] == 'B':
        matrix[snake_r][snake_c] = '.'
        for row in matrix:
            if 'B' in row:
                snake_r = matrix.index(row)
                snake_c = row.index('B')
    matrix[snake_r][snake_c] = 'S'
if food == 10:
    print('You won! You fed the snake.')
print(f'Food eaten: {food}')
for row in matrix:
    print(''.join(row))
