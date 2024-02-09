rows, columns = [int(x) for x in input().split()]
matrix = [list(map(int, input().split())) for _ in range(rows)]
biggest_sum = -21
biggest_matrix = []
for i in range(rows - 2):
    for j in range(columns - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
                      matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
                      matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                              [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                              [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
print(f'Sum = {biggest_sum}')
for row in biggest_matrix:
    print(*row)