
def even_parameters(func):
    def wrapper(*args, **kwargs):

        for arg in args:
            if not (isinstance(arg, int) or isinstance(arg, float)) or not arg % 2 == 0:
                return 'Please use only even numbers!'

        return func(*args, **kwargs)
    return wrapper


@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))

print(add("Peter", 1))
