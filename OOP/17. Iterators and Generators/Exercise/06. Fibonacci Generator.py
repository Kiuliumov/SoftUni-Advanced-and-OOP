def fibonacci():
    current = 0
    last_num = 1

    while True:
        current_last_num = last_num
        last_num = current
        yield current
        current = current + current_last_num




generator = fibonacci()
for i in range(5):
    print(next(generator))
