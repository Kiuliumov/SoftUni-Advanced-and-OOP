from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(';'):
    name,time_needed = r.split('-')
    robots[name] = [time_needed,0]
factory_time = datetime.strptime(input())
products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    factory_time += timedelta(0,1)
    free_robots = []
    product = products.popleft()
    for name,value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1
        else:
            free_robots.append([name,value])
    if not free_robots:
        products.append(product)
        continue
    robots_name,data = free_robots[0]
