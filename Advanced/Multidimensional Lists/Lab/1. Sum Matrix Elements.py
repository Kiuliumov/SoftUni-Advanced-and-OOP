rows, cols = [int(x) for x in input().split(", ")]
current_sum = 0
matrix = []


for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)
    current_sum += sum(lines)

print(current_sum)
print(matrix)