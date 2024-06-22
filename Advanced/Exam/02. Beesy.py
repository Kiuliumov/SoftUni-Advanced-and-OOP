def find_start(matrix):


    STARTER = 'B'

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == STARTER:
                return (i, j)


def handle_movement(current_row, current_col, command, n):
    if command == 'up':
        if current_row - 1 < 0:
            current_row = n - 1
        else:
            current_row -= 1

    elif command == 'down':
        if current_row + 1 >= n:
            current_row = 0
        else:
            current_row += 1

    elif command == 'left':
        if current_col - 1 < 0:
            current_col = n - 1
        else:
            current_col -= 1

    elif command == 'right':
        if current_col + 1 >= n:
            current_col = 0
        else:
            current_col += 1

    return current_row, current_col




n = int(input())
grid = [list(input()) for _ in range(n)]

coordinates = find_start(grid)
row, col = coordinates

energy = 15
collected_nectar = 0
jockey_card = False


while True:
    grid[row][col] = '-'
    command = input()
    energy -= 1
    coordinates = handle_movement(row, col, command, n)
    row, col = coordinates

    if grid[row][col].isdigit():
        collected_nectar += int(grid[row][col])
        grid[row][col] = '-'

    elif grid[row][col] == 'H':
        if collected_nectar >= 30:
            print('Great job, Beesy! The hive is full. Energy left: {}'.format(energy))
            break
        else:
            print('Beesy did not manage to collect enough nectar.')
            break

    if energy == 0 and collected_nectar > 30 and not jockey_card:
        jockey_card = True
        energy = collected_nectar - 30
        collected_nectar = 30
    elif energy == 0:
        print('This is the end! Beesy ran out of energy.')
        break

grid[row][col] = 'B'
for row in grid:
    print(''.join(row))
