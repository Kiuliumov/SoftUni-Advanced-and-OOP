rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

max_sum = float('-inf')
max_submatrix = None

for i in range(rows - 1):
    for j in range(columns - 1):
        submatrix_sum = sum(matrix[i][j:j+2]) + sum(matrix[i+1][j:j+2])
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j], matrix[i+1][j+1]]]
for row in max_submatrix:
    print(*row)
print(max_sum)
