import timeit


def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        t = timeit.timeit(lambda: func(*args, **kwargs))
        print(f'{func.__name__} call took: {t:.2f} sec')
        print(func.__name__+' result:', func(*args, **kwargs))
    return wrapper

def n_plus_1(n):
    result = n+1
    return result

def n_mines_1(n):
    result = n-1
    return result

plus1 = measure_elapsed_time(n_plus_1)
mines1 = measure_elapsed_time(n_mines_1)



plus1(5)
mines1(5)
