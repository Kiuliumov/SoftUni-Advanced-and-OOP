from collections import deque

rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
bomb_coordinates = deque(input().split())

while bomb_coordinates:
    current_bomb_coordinates = bomb_coordinates.popleft()
    row = int(current_bomb_coordinates[0])
    column = int(current_bomb_coordinates[2])
    current_bomb = matrix[row][column]
    if current_bomb > 0:
        matrix[row][column] = 0
        if row + 1 < rows:
            if matrix[row + 1][column] > 0:
                matrix[row + 1][column] -= current_bomb
        if row - 1 >= 0:
            if matrix[row - 1][column] > 0:
                matrix[row - 1][column] -= current_bomb
        if row + 1 < rows and column + 1 < rows:
            if matrix[row + 1][column + 1] > 0:
                matrix[row + 1][column + 1] -= current_bomb
        if row - 1 >= 0 and column + 1 < rows:
            if matrix[row - 1][column + 1] > 0:
                matrix[row - 1][column + 1] -= current_bomb
        if row + 1 < rows and column - 1 >= 0:
            if matrix[row + 1][column - 1] > 0:
                matrix[row + 1][column - 1] -= current_bomb
        if row - 1 >= 0 and column - 1 >= 0:
            if matrix[row - 1][column - 1] > 0:
                matrix[row - 1][column - 1] -= current_bomb
        if column - 1 >= 0:
            if matrix[row][column - 1] > 0:
                matrix[row][column - 1] -= current_bomb
        if column + 1 < rows:
            if matrix[row][column + 1] > 0:
                matrix[row][column + 1] -= current_bomb

count_of_alive_cells = 0
sum_of_alive_cells = 0
for row in range(rows):
    for column in range(rows):
        if matrix[row][column] > 0:
            count_of_alive_cells += 1
            sum_of_alive_cells += matrix[row][column]

print(f'Alive cells: {count_of_alive_cells}')
print(f'Sum: {sum_of_alive_cells}')

for row in range(rows):
    print(*matrix[row])
