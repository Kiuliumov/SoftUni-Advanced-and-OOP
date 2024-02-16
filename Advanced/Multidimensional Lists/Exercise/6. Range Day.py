matrix = [input().split() for _ in range(5)]
n = int(input())
player_r, player_c = None, None
all_targets = 0
for row in matrix:
    if 'A' in row:
        player_r = matrix.index(row)
        player_c = row.index('A')
    if 'x' in row:
        all_targets += row.count('x')
matrix[player_r][player_c] = '.'
hit_targets = []
for _ in range(n):
    command, *rest = input().split()
    if command == 'move':
        direction, squares = rest
        squares = int(squares)
        if direction == 'up':
            if player_r - squares >= 0 and matrix[player_r - squares][player_c] == '.':
                player_r -= squares
        elif direction == 'down':
            if player_r + squares < len(matrix) and matrix[player_r + squares][player_c] == '.':
                player_r += squares
        elif direction == 'left':
            if player_c - squares >= 0 and matrix[player_r][player_c - squares] == '.':
                player_c -= squares
        elif direction == 'right':
            if player_c + squares < len(matrix[player_r]) and matrix[player_r][player_c + squares] == '.':
                player_c += squares
    elif command == 'shoot':
        direction = rest[0]
        if direction == 'up':
            for row in range(player_r, -1, -1):
                if matrix[row][player_c] == 'x':
                    hit_targets.append([row, player_c])
                    all_targets -= 1
                    break
        elif direction == 'down':
            for row in range(player_r + 1, len(matrix)):
                if matrix[row][player_c] == 'x':
                    hit_targets.append([row, player_c])
                    all_targets -= 1
                    break
        elif direction == 'left':
            for col in range(player_c, -1, -1):
                if matrix[player_r][col] == 'x':
                    hit_targets.append([player_r, col])
                    all_targets -= 1
                    break
        elif direction == 'right':
            for col in range(player_c, len(matrix[player_r])):
                if matrix[player_r][col] == 'x':
                    all_targets -= 1
                    hit_targets.append([player_r, col])
                    break
if not all_targets:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f'Training not completed! {all_targets} targets left.')
for target in hit_targets:
    print(target)
