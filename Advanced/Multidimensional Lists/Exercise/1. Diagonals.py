n = int(input())
matrix = []

for i in range(n):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

primary_diagonal = []
secondary_diagonal = []


for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-(i + 1)])


print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
