from collections import deque

worms = deque(map(int, input().split()))
holes = deque(map(int, input().split()))
initial_worms = len(worms)
matches = 0

while worms and holes:
    last_worm = worms.pop()
    if last_worm <= 0:
        continue
    first_hole = holes.popleft()
    if last_worm == first_hole:
        matches += 1
    else:
        if last_worm - 3 > 0:
            worms.append(last_worm - 3)
flag = False
if matches:
    print("Matches:", matches)
else:
    print('There are no matches.')
if not worms and matches == initial_worms:
    print("Every worm found a suitable hole!")
    flag = True
if not flag:
    print(f"Worms left: {(', '.join([str(x) for x in worms]) if worms else 'none')} ")
print(f"Holes left: {(', '.join([str(x) for x in holes]) if holes else 'none')} ")

