rows = int(input())
matrix = [input().split() for _ in range(rows)]
most_eggs_collected = float('-inf')
best_direction = None
bunny_x = None
bunny_y = None
collected_eggs_coordinates = []

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == 'B':
            bunny_y = row
            bunny_x = col

directions = ['up', 'down', 'left', 'right']

for direction in directions:
    current_points = 0
    temp_x, temp_y = bunny_x, bunny_y
    collected_eggs_direction = []
    for _ in range(rows):
        if direction == 'up':
            if temp_y - 1 >= 0 and matrix[temp_y - 1][temp_x] != 'X':
                temp_y -= 1
                current_points += int(matrix[temp_y][temp_x])
                collected_eggs_direction.append([temp_y, temp_x])

        elif direction == 'down':
            if temp_y + 1 < rows and matrix[temp_y + 1][temp_x] != 'X':
                temp_y += 1
                current_points += int(matrix[temp_y][temp_x])
                collected_eggs_direction.append([temp_y, temp_x])

        elif direction == 'left':
            if temp_x - 1 >= 0 and matrix[temp_y][temp_x - 1] != 'X':
                temp_x -= 1
                current_points += int(matrix[temp_y][temp_x])
                collected_eggs_direction.append([temp_y, temp_x])

        elif direction == 'right':
            if temp_x + 1 < rows and matrix[temp_y][temp_x + 1] != 'X':
                temp_x += 1
                current_points += int(matrix[temp_y][temp_x])
                collected_eggs_direction.append([temp_y, temp_x])

    if current_points > most_eggs_collected:
        most_eggs_collected = current_points
        best_direction = direction
        collected_eggs_coordinates = collected_eggs_direction[:]

print(best_direction)
for coordinate in collected_eggs_coordinates:
    print([coordinate[0], coordinate[1]])
print(most_eggs_collected)
