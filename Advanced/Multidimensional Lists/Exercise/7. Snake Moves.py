from collections import deque

rows, cols = list(map(int, input().split()))
snake = list(input())
word_copy = deque(snake)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(snake)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[word_copy.pop() for _ in range(cols)][::-1], sep='')
