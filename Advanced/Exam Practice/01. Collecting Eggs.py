from collections import deque
eggs = deque([int(x) for x in input().split(', ') if int(x) > 0])
paper = deque(map(int,input().split(', ')))
filled_boxes = 0
while eggs and paper:
    first_egg = eggs.popleft()
    last_paper = paper.pop()
    if first_egg == 13:
        first_paper = paper.popleft()
        paper.append(first_paper)
        paper.appendleft(last_paper)
    else:
        if first_egg + last_paper <= 50:
            filled_boxes += 1
if filled_boxes:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    eggs = [str(x) for x in eggs]
    print(f'Eggs left: {", ".join(eggs)}')
if paper:
    paper = [str(x) for x in paper]
    print(f'Pieces of paper left: {", ".join(paper)} ')