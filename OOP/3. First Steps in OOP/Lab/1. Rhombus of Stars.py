def print_line(n, i):
    print(' ' * (n - i), end="")
    print(*['*'] * i)


def draw_top(n):
    for i in range(1, n + 1):
        print_line(n, i)


def draw_bottom(n):
    for i in range(n - 1, 0, -1):
        print_line(n, i)


def draw(number):
    draw_top(number)
    draw_bottom(number)


n = int(input())
draw(n)
