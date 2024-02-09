rows,columns = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]
count = 0
for i in range(rows - 1):
    for j in range(columns - 1):
        if len({matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]}) == 1:
            count += 1
print(count)