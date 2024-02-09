rows = int(input())
final_list = []
for i in range(rows):
    line = [int(x) for x in input().split(', ')]
    final_list.extend(line)
print(final_list)