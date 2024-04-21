from collections import deque

contests = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contests and pies:
    current_contest = contests.popleft()
    current_pie = pies.pop()

    if current_contest >= current_pie:
        current_contest -= current_pie

        if current_contest == 0:
            continue
        contests.append(current_contest)

    else:
        current_pie -= current_contest
        if current_pie == 1:
            if pies:
                pies[-1] += 1
                continue
        pies.append(current_pie)

if not pies and contests:
    print('We will have to wait for more pies to be baked!')
    print('Contestants left: {}'.format(', '.join([str(c) for c in contests])))

elif not pies and not contests:
    print('We have a champion!')

else:
    print('Our contestants need to rest!')
    print('Pies left: {}'.format(', '.join([str(pie) for pie in pies])))
