n = int(input())
tank = 0
smallest_point = 0
for number_of_station in range(n):
    amount_of_petrol,distance = [int(x) for x in input().split()]
    tank += amount_of_petrol
    tank -= distance
    if tank < 0:
        smallest_point = number_of_station + 1
        tank = 0
print(smallest_point)