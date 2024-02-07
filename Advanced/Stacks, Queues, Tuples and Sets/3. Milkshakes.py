chocolates = list(map(int, input().split(', ')))
cups_of_milk = list(map(int, input().split(', ')))
milkshakes = 0
while milkshakes != 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates[-1]
    current_milk = cups_of_milk[0]
    if current_chocolate <= 0 or current_milk <= 0:
        if current_chocolate <= 0:
            chocolates.pop()
        if current_milk <= 0:
            cups_of_milk.pop(0)
        continue
    if current_milk == current_chocolate:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.pop(0)
    else:
        cups_of_milk.append(cups_of_milk.pop(0))
        chocolates[-1] -= 5
if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
print('Chocolate:', ', '.join(map(str, chocolates)) if chocolates else 'empty')
print('Milk:', ', '.join(map(str, cups_of_milk)) if cups_of_milk else 'empty')