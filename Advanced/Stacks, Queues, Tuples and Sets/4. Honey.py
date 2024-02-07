from collections import deque
working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())
total_honey = 0
while working_bees and nectar:
    bee = working_bees.popleft()
    total_nectar = 0

    while nectar and nectar[-1] < bee:
        total_nectar += nectar.pop()

    if nectar and nectar[-1] >= bee:
        total_nectar = nectar.pop()

    symbol = symbols.popleft()

    if symbol == '/' and total_nectar == 0:
        continue
    else:
        total_honey += abs(eval(f'{bee} {symbol} {total_nectar}'))

print(f'Total honey made: {total_honey}')

if working_bees:
    print('Bees left:', ', '.join(map(str, working_bees)))

if nectar:
    print('Nectar left:', ', '.join(map(str, nectar)))