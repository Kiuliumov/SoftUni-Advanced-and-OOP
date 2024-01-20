given_array = input().split(' ')
stack = []
while given_array:
    stack.append(given_array.pop())
print(*stack)