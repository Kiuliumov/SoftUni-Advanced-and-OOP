size = int(input())
matrix = []
for i in range(size):
    matrix.append(list(input()))

character = input()
row_position = None
char_position = None

for i in range(size):
    row = matrix[i]
    if character in row:
        row_position = i
        char_position = row.index(character)
        final_tuple = (row_position, char_position)
        print(final_tuple)
        break

else:
    print(f'{character} does not occur in the matrix')
