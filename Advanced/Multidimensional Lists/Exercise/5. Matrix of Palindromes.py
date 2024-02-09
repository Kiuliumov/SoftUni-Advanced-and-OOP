rows, columns = map(int, input().split())
start_char = ord('a')

for i in range(rows):
    row = []
    for j in range(columns):
        middle_char = chr(start_char + i + j)
        palindrome = chr(start_char + i) + middle_char + chr(start_char + i)
        row.append(palindrome)
    print(" ".join(row))
