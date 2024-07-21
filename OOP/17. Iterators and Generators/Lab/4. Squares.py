def squares(n):
    i = 1
    while i <= n:
        i += 1
        yield i * i

print(list(squares(5)))