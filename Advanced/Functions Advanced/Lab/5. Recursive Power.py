def recursive_power(x,y):
    result = 1
    if y == 0:
        return result
    else:
        result = x * recursive_power(x,y-1)
        return result