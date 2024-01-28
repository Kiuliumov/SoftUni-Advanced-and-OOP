n = int(input())
odd_set = set()
even_set = set()
for counter in range(1,n + 1):
    sum_of_chars = 0
    name = input()
    for char in name:
        sum_of_chars += ord(char)
    sum_of_chars //= counter
    if sum_of_chars % 2 == 0:
        even_set.add(sum_of_chars)
    else:
        odd_set.add(sum_of_chars)
if sum(odd_set) == sum(even_set):
    print(*(odd_set | even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')


