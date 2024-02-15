n = int(input())
matrix = [input().split() for _ in range(n)]
tea_bags = 0
alice_r = None
alice_c = None
for row in range(n):
    if 'A' in matrix[row]:
        alice_r = row
        alice_c = matrix[row].index('A')
enough_tea = False
while not enough_tea:
    matrix[alice_r][alice_c] = '*'
    command = input()
    # movement logic
    if command == 'up':
        if alice_r - 1 < 0:
            break
        else:
            alice_r -= 1
    elif command == 'down':
        if alice_r + 1 >= n:
            break
        else:
            alice_r += 1
    elif command == 'left':
        if alice_c - 1 < 0:
            break
        else:
            alice_c -= 1
    elif command == 'right':
        if alice_c + 1 >= n:
            break
        else:
            alice_c += 1
    # checking logic
    if matrix[alice_r][alice_c].isdigit():
        tea_bags += int(matrix[alice_r][alice_c])
        if tea_bags >= 10:
            enough_tea = True
            matrix[alice_r][alice_c] = '*'
    elif matrix[alice_r][alice_c] == 'R':
         matrix[alice_r][alice_c] = '*'
         break
    else:
        matrix[alice_r][alice_c] = '*'
if enough_tea:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row)