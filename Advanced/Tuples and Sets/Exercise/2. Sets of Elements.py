n_set = set()
m_set = set()
n,m = (int(x) for x in input().split())
for _ in range(n):
    n_set.add(int(input()))
for _ in range(m):
    m_set.add(int(input()))
for item in n_set:
    if item in m_set:
        print(item)
