turns = input().split(', ')
skipped = []
rows = 6
matrix = [input().split() for _ in range(6)]
current_turn = 0 if turns[0] == 'T' else 1

while True:
    stored = input()
    row, col = int(stored[1]), int(stored[4])
    current = turns.pop(0)
    if current not in skipped:
        if matrix[row][col] == 'E':
            print(f'{current} found the Exit and wins the game!')
            break
        elif matrix[row][col] == 'T':
            print(f'{current} is out of the game! The winner is {turns[0]}.')
            break
        elif matrix[row][col] == 'W':
            skipped.append(current)
            print(f'{current} hits a wall and needs to rest.')
    else:
        skipped.pop(0)
    turns.append(current)
