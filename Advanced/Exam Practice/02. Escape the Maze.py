STARTING_POSITION = 'P'
EXIT = 'X'
MONSTER = 'M'
HEALTH_POTION = 'H'
SPACE = '-'
CURRENT_HEALTH = 100
VALID_COMMANDS = ['up', 'down', 'left', 'right']


def find_player(board) -> dict:
    player_coordinates = {'r': 0, 'c': 0}

    for row in board:
        if STARTING_POSITION in row:
            player_coordinates['r'] = board.index(row)
            player_coordinates['c'] = row.index(STARTING_POSITION)
            break
    return player_coordinates


n = int(input())
matrix = [list(input()) for _ in range(n)]
player_coordinates = find_player(matrix)
player_exited = False

while CURRENT_HEALTH > 0 and not player_exited:
    r = player_coordinates['r']
    c = player_coordinates['c']
    matrix[r][c] = '-'
    command = input()

    if command == 'up':
        if r - 1 >= 0:
            player_coordinates['r'] -= 1
    elif command == 'down':
        if r + 1 < len(matrix):
            player_coordinates['r'] += 1
    elif command == 'left':
        if c - 1 >= 0:
            player_coordinates['c'] -= 1
    elif command == 'right':
        if c + 1 < len(matrix[0]):
            player_coordinates['c'] += 1

    r = player_coordinates['r']
    c = player_coordinates['c']
    current_position = matrix[r][c]

    if current_position == MONSTER:
        CURRENT_HEALTH -= 40
        matrix[r][c] = 'P'
        if CURRENT_HEALTH < 0:
            break

    if current_position == HEALTH_POTION:
        if CURRENT_HEALTH > 85:
            CURRENT_HEALTH = 100
        else:
            CURRENT_HEALTH += 15
        matrix[r][c] = 'P'

    if current_position == EXIT:
        matrix[r][c] = 'P'
        break

if CURRENT_HEALTH < 0:
    print('Player is dead. Maze over!')
else:
    print('Player escaped the maze. Danger passed!')
print("Player's health: {} units".format(str(CURRENT_HEALTH) if CURRENT_HEALTH > 0 else 0))
for row in matrix:
    print(''.join(row))
