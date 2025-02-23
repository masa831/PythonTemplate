import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


# test functions ###############
@timing_decorator
def test_decorator(a, b, c):
    a = add(a, b)
    b = add3(a, b, c)
    return a + b


# Example usage
@logging_decorator
def add(a, b):
    return a + b


@logging_decorator
def add3(a, b, c):
    return a + b + c
