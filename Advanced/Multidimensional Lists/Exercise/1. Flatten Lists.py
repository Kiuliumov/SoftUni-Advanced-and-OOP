# oop style
given_list = reversed([x.strip().split() for x in input().split('|')])
flattened_list = [item for sublist in given_list for item in sublist]
for item in flattened_list:
    print(item, end=' ')
