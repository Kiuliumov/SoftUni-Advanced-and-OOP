from collections import deque
command = input()
people = deque()
while command != 'End':
    if command == 'Paid':
        while people:
            print(people.popleft())
    else:
        people.append(command)
    command = input()
print(f'{len(people)} people remaining.')
