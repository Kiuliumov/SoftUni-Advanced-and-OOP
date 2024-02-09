size = int(input())
matrix = []
diagonal_sum = 0
for i in range(size):
    matrix.append([int(x) for x in input().split()])
for i in range(size):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
