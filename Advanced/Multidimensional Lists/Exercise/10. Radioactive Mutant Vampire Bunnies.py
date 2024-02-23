from collections import deque

rows, cols = [int(x) for x in input().split()]
lair = [list(input()) for _ in range(rows)]
instructions = deque(input())

player_x = None
player_y = None
found_bunny = False
won = False

for row in lair:
    if 'P' in row:
        player_r = row
        player_c = row.index('P')
