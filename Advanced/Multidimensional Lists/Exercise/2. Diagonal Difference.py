n = int(input())
matrix = []

for i in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)

primary_diagonal = []
secondary_diagonal = []


for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][-(i + 1)])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))