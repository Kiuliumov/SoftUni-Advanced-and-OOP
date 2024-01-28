n = int(input())
biggest_intersection = set()
for _ in range(n):
    ranges = input().split('-')
    first_range = ranges[0].split(',')
    second_range = ranges[1].split(',')
    first_element = int(first_range[0])
    second_element = int(first_range[1]) + 1
    third_element = int(second_range[0])
    forth_element = int(second_range[1]) + 1
    first_range = set(range(first_element,second_element))
    second_range = set(range(third_element, forth_element))
    intersection = first_range & second_range
    if len(intersection) > len(biggest_intersection):
        biggest_intersection = intersection
print(f'Longest intersection is {list(biggest_intersection)} with length {len(biggest_intersection)}')
