def tags(tag):
    def decorator(func):

        def wrapper(*args, **kwargs):
            return '<' + tag + '>' + func(*args, **kwargs) + '</' + tag + '>'

        return wrapper
    return decorator

