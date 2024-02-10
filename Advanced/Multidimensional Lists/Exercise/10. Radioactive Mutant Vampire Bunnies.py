from collections import deque

rows, cols = [int(x) for x in input().split()]
lair = [list(input()) for _ in range(rows)]
instructions = deque(input())

player_x = None
player_y = None
found_bunny = False
won = False

for row in range(rows):
    for col in range(cols):
        if lair[row][col] == 'P':
            player_y = row
            player_x = col

while instructions and not found_bunny and not won:
    multiplied_bunnies = set()
    current_instruction = instructions.popleft()

    if current_instruction == 'U':
        if player_y - 1 >= 0:
            player_y -= 1
    elif current_instruction == 'D':
        if player_y + 1 < rows:
            player_y += 1
    elif current_instruction == 'L':
        if player_x - 1 >= 0:
            player_x -= 1
    elif current_instruction == 'R':
        if player_x + 1 < cols:
            player_x += 1

    if lair[player_y][player_x] == 'B':
        found_bunny = True

    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'B' and (row, col) not in multiplied_bunnies:
                if row + 1 < rows and lair[row + 1][col] == '.':
                    lair[row + 1][col] = 'B'
                    multiplied_bunnies.add((row + 1, col))
                if row - 1 >= 0 and lair[row - 1][col] == '.':
                    lair[row - 1][col] = 'B'
                    multiplied_bunnies.add((row - 1, col))
                if col + 1 < cols and lair[row][col + 1] == '.':
                    lair[row][col + 1] = 'B'
                    multiplied_bunnies.add((row, col + 1))
                if col - 1 >= 0 and lair[row][col - 1] == '.':
                    lair[row][col - 1] = 'B'
                    multiplied_bunnies.add((row, col - 1))

if won:
    lair[player_y][player_x] = '.'

for row in lair:
    print(''.join(row))

if found_bunny:
    print(f'dead: {player_y} {player_x}')
else:
    print(f'won: {player_y} {player_x}')
