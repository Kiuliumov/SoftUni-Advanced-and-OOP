def type_check(type):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for arg in args:
                if not isinstance(arg, type):
                    return 'Bad Type'
            return func(*args, **kwargs)

        return wrapper

    return decorator

