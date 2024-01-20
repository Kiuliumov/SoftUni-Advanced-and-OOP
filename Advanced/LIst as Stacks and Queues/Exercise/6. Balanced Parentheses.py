parentheses = list(input())
are_balanced = True
stack = []
mapping = {')':'(','}':'{',']':'['}
for i in parentheses:
    if i in mapping.values():
        stack.append(i)
    elif i in mapping.keys():
        if not stack or stack.pop() != mapping[i]:
          are_balanced = False
if are_balanced:
    print('YES')
else:
    print('NO')

