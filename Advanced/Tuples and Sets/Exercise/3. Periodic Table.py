n = int(input())
table = set()
for _ in range(n):
    for compound in input().split():
        table.add(compound)
for compound in table:
    print(compound)