numbers = map(int,input().split())
target = int(input())

targets = set()
hashmap = {}

for value in numbers:
    resulting_number = target - value
    targets.add(resulting_number)
    hashmap[resulting_number] = value
for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = hashmap[value]
        del hashmap[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        hashmap[resulting_number] = value
