import timeit


def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        # t = timeit.timeit(lambda: func(*args, **kwargs))
        func(*args, **kwargs)
        end = timeit.default_timer()
        t = end-start
        print(f'{func.__name__} call took: {t:.6} sec')

    return wrapper

def n_plus_1(n):
    result = n+1
    print('n_plus_1 result:', result)

def n_mines_1(n):
    result = n-1
    print('n_mines_1 result:', result)

plus1 = measure_elapsed_time(n_plus_1)
mines1 = measure_elapsed_time(n_mines_1)



plus1(5)
mines1(5)
