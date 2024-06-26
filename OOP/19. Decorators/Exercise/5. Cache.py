def cache(func):
    log = {}

    def wrapper(n):

        if n not in log:
            log[n] = func(n)

        return log[n]
    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


