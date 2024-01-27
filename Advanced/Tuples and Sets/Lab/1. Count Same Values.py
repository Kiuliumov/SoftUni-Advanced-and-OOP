nums = list(map(int,input().split(' ')))
seen_nums = []
for num in nums:
    if num not in seen_nums:
        print(f'{num:.1f} - {nums.count(num)} times')
        seen_nums.append(num)