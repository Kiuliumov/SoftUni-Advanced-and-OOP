rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
command = input()
while command != 'END':
    command, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if 0 <= row < rows and 0 <= col < rows:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input()
for row in matrix:
    print(*row)