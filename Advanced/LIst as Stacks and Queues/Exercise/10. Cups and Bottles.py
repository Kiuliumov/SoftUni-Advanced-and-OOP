from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0
while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_cup > current_bottle:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    else:
        wasted_water += current_bottle - current_cup
if not cups:
    bottles = list(reversed(bottles))
    print('Bottles:',*bottles)
else:
    print('Cups:',*cups)
print(f'Wasted litters of water: {wasted_water}')