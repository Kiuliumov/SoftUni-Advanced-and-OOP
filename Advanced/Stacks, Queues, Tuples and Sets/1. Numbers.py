#exercise
first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())
n = int(input())
for _ in range(n):
    user_input = input().split()
    command = user_input[0] + ' ' + user_input[1]
    numbers = [int(num) for num in user_input[2:]]
    if command == 'Add First':
        first.update(numbers)
    if command == 'Add Second':
        second.update(numbers)
    if command == 'Remove First':
        first.difference_update(numbers)
    if command == 'Remove Second':
        second.difference_update(numbers)
    if command == 'Check Subset':
        if first.issubset(second) or second.issubset(first):
            print('True')
        else:
            print('False')
print(*sorted(first),sep=', ')
print(*sorted(second),sep=', ')
