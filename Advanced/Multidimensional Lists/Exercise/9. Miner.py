from collections import deque

rows = int(input())
instructions = deque(input().split())
game_board = [input().split() for _ in range(rows)]


coal = 0
ended = False
miner_x = None
miner_y = None

for row in range(rows):
    for col in range(rows):
        if game_board[row][col] == 's':
            miner_y, miner_x = row, col
        if game_board[row][col] == 'c':
            coal += 1

while instructions and not ended:
    current_instruction = instructions.popleft()
    if current_instruction == 'up' and miner_y - 1 >= 0:
        miner_y -= 1
    elif current_instruction == 'down' and miner_y + 1 < rows:
        miner_y += 1
    elif current_instruction == 'left' and miner_x - 1 >= 0:
        miner_x -= 1
    elif current_instruction == 'right' and miner_x + 1 < rows:
        miner_x += 1

    if game_board[miner_y][miner_x] == 'e':
        ended = True
    elif game_board[miner_y][miner_x] == 'c':
        coal -= 1
        game_board[miner_y][miner_x] = '*'

    if coal == 0:
        break

if ended:
    print(f'Game over! {miner_y, miner_x}')
else:
    if coal:
        print(f'{coal} pieces of coal left. {miner_y, miner_x}')
    else:
        print(f'You collected all coal! {miner_y, miner_x}')
