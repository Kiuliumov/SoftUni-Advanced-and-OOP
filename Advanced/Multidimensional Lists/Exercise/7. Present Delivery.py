presents = int(input())
n = int(input())
matrix = [input().split() for _ in range(n)]
santa_r, santa_c = None, None
initial_nice_kids = 0
for row in matrix:
    if 'S' in row:
        santa_r = matrix.index(row)
        santa_c = row.index('S')
    if 'V' in row:
        initial_nice_kids += row.count('V')
while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_r][santa_c] = '-'
    if command == 'up':
        santa_r -= 1
    elif command == 'down':
        santa_r += 1
    elif command == 'left':
        santa_c -= 1
    elif command == 'right':
        santa_c += 1
    current_position = matrix[santa_r][santa_c]
    if current_position == 'V':
        matrix[santa_r][santa_c] = 'S'
        presents -= 1
        if not presents:
            break
    elif current_position == 'C':
        matrix[santa_r][santa_c] = 'S'
        # up
        if matrix[santa_r - 1][santa_c] in ['V', 'X']:
            matrix[santa_r - 1][santa_c] = '-'
            presents -= 1
            if not presents:
                break
            # down
        if matrix[santa_r + 1][santa_c] in ['V', 'X']:
            matrix[santa_r + 1][santa_c] = '-'
            presents -= 1
            if not presents:
                break
            # left
        if matrix[santa_r][santa_c - 1] in ['V', 'X']:
            matrix[santa_r][santa_c - 1] = '-'
            presents -= 1
            if not presents:
                break
            # right
        if matrix[santa_r][santa_c + 1] in ['V', 'X']:
            matrix[santa_r][santa_c + 1] = '-'
            presents -= 1
            if not presents:
                break
nice_kids = 0
for row in matrix:
    if 'V' in row:
        nice_kids += row.count('V')

if nice_kids and not presents:
    print('Santa ran out of presents!')
for row in matrix:
    print(' '.join(row).strip())
if not nice_kids:
    print(f'Good job, Santa! {initial_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')
