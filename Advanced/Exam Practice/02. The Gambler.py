n = int(input())
current_money = 100
matrix = [list(input()) for _ in range(n)]
gambler_r,gambler_c = None,None
for i in range(len(matrix)):
    row = matrix[i]
    if 'G' in row:
        gambler_r = i
        gambler_c = row.index('G')
command = input()
lost = False
won = False
while command != 'end' and not lost and not won:
    matrix[gambler_r][gambler_c] = '-'
    try:
        if command == 'up':
            gambler_r -= 1
        elif command == 'down':
            gambler_r += 1
        elif command == 'left':
            gambler_c -= 1
        elif command == 'right':
            gambler_c += 1
        current_position = matrix[gambler_r][gambler_c]
        if current_position == 'W':
            current_money += 100
        elif current_position == 'P':
            if current_money - 200 <= 0:
                lost = True
            else:
                current_money -= 200
        elif current_position == 'J':
            current_money += 100000
            won = True
        matrix[gambler_r][gambler_c] = 'G'
        command = input()
    except IndexError:
        lost = True
if won:
    print(f'You win the Jackpot!End of the game. Total amount: {current_money}$')
if not won and not lost:
    print(f'End of the game. Total amount: {current_money}$')
if lost:
    print('Game over! You lost everything!')
if not lost:
    for row in matrix:
        print(''.join(row))



