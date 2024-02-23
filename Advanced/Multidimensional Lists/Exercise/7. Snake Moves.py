from collections import deque

r, c = map(int, input().split())
snake = input().strip()

snake_queue = deque(snake)
capacity = r * c

for i in range(r):
    row = []
    for j in range(c):
        if snake_queue:
            if i % 2 == 0:
                row.append(snake_queue.popleft())
            else:
                row.insert(0, snake_queue.pop())
    print("".join(row))
