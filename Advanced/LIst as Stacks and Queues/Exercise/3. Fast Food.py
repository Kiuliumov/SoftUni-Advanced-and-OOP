from collections import deque
quantity = int(input())
orders = deque(map(int, input().split(' ')))
print(max(orders))
while orders:
    max_order = max(orders)
    if quantity >= max_order:
        quantity -= orders.popleft()
    else:
        print('Orders left:', *orders)
        break
else:
    print('Orders complete')
