rows, columns = [int(x) for x in input().split(',')]
grid = [list(input()) for _ in range(rows)]
mouse_x = None
mouse_y = None
lost = False
cheese = 0

for row in range(rows):
    for col in range(columns):
        if grid[row][col] == 'M':
            mouse_x = row
            mouse_y = col
        elif grid[row][col] == 'C':
            cheese += 1

command = input()
while command != 'danger':
    grid[mouse_x][mouse_y] = '*'
    if command == 'up':
        if mouse_x - 1 < 0:
            lost = True
        elif grid[mouse_x - 1][mouse_y] == '@':
            pass
        else:
            mouse_x -= 1
    elif command == 'down':
        if mouse_x + 1 >= rows:
            lost = True
        elif grid[mouse_x + 1][mouse_y] == '@':
            pass
        else:
            mouse_x += 1
    elif command == 'left':
        if mouse_y - 1 < 0:
            lost = True
        elif grid[mouse_x][mouse_y - 1] == '@':
            pass
        else:
            mouse_y -= 1
    elif command == 'right':
        if mouse_y + 1 >= columns:
            lost = True
        elif grid[mouse_x][mouse_y + 1] == '@':
            pass
        else:
            mouse_y += 1

    if lost:
        print('No more cheese for tonight!')
        break

    if grid[mouse_x][mouse_y] == 'C':
        grid[mouse_x][mouse_y] = '*'
        cheese -= 1
        if cheese == 0:
            print('Happy mouse! All the cheese is eaten, good night!')
            break
    elif grid[mouse_x][mouse_y] == 'T':
        print('Mouse is trapped!')
        break
    command = input()
else:
    if cheese:
        print('Mouse will come back later!')
grid[mouse_x][mouse_y] = 'M'
for row in grid:
    print(''.join(row))
