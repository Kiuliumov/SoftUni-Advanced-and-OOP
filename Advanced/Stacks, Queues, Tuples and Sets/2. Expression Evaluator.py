from collections import deque
from math import floor
given_array = deque(input().split())
operations = ['*', '+', '-', '/']
current_items = deque([])
while given_array:
    item = given_array.popleft()
    if item in operations:
        if item == '*':
            result = 1
            for item in current_items:
                result *= item
            given_array.appendleft(result)
            current_items.clear()
        if item == '+':
            result = sum(current_items)
            given_array.appendleft(result)
            current_items.clear()
        if item == '-':
            result = current_items.popleft()
            for item in current_items:
                result -= item
            given_array.appendleft(result)
            current_items.clear()
        if item == '/':
            result = current_items.popleft()
            for item in current_items:
                result /= item
            given_array.appendleft(floor(result))
            current_items.clear()
    else:
        current_items.append(int(item))
print(item)