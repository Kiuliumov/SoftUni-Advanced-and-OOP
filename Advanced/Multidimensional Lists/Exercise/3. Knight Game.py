



rows = int(input())
matrix = [list(input()) for _ in range(rows)]
knights_removed = 0


def count_attacks(row, col):
    attacks = 0
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    for dx, dy in directions:
        x, y = row + dx, col + dy
        if 0 <= x < rows and 0 <= y < rows and matrix[x][y] == 'K':
            attacks += 1
    return attacks


while True:
    max_attacks = 0
    max_i, max_j = -1, -1

    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'K':
                attacks = count_attacks(i, j)
                if attacks > max_attacks:
                    max_attacks = attacks
                    max_i, max_j = i, j

    if max_attacks == 0:
        break

    matrix[max_i][max_j] = '0'
    knights_removed += 1

print(knights_removed)
