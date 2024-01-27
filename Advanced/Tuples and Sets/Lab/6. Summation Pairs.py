numbers = map(int, input().split())
target = int(input())

targets = set()
hashmap = {}

for value in numbers:
    resulting_number = target - value
    if value in targets:
        pair = hashmap[value]
        print(f'{pair} + {value} = {target}')
    else:
        targets.add(resulting_number)
        hashmap[resulting_number] = value
