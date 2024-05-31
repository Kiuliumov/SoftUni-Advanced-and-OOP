def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'you called {func.__name__}({", ".join([str(arg) for arg in args])})\nit returned {result}'
    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))