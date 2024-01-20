from collections import deque
kids = deque(input().split(' '))
n = int(input()) - 1
while len(kids) != 1:
    kids.rotate(-n)
    hot_potato = kids.popleft()
    print(f'{hot_potato} had the hot potato!')
print(f'Last is {kids.popleft()}')