expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        start_ind = int(stack.pop())
        end_index = i + 1
        print(expression[start_ind:end_index])
