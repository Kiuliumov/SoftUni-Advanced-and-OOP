vip = set()
regular = set()

n = int(input())
for _ in range(n):
    id = input()
    if len(id) != 8:
        continue
    if id[0].isdigit():
        vip.add(id)
    else:
        regular.add(id)

command = input()
while command != 'END':
    if command[0].isdigit() and command in vip:
        vip.remove(command)
    elif command in regular:
        regular.remove(command)
    command = input()

print(len(vip) + len(regular))
for person in sorted(vip):
    print(person)
for person in sorted(regular):
    print(person)
