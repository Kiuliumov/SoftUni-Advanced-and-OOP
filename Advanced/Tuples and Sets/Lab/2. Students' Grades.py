n = int(input())
results = {}
for _ in range(n):
    name,grade = input().split(' ')
    grade = float(grade)
    if name not in results:
        results[name] = []
    results[name].append(grade)
for name,grades in results.items():
    average_grades = sum(grades)/len(grades)
    grades = [f'{grade:.2f}' for grade in grades]
    print(f'{name} -> {" ".join(grades)} (avg: {average_grades:.2f})')