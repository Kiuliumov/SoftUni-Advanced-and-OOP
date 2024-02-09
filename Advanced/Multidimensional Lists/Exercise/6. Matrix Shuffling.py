rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    tokens = command.split()
    if tokens[0] == 'swap' and len(tokens) == 5:
        coordinates = list(map(int, tokens[1:]))
        row1, col1, row2, col2 = coordinates
        if 0 <= row1 < rows and 0 <= col1 < columns and 0 <= row2 < rows and 0 <= col2 < columns:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    command = input()
