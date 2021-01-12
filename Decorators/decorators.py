# function decorator
import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@start_end_decorator
def print_name():
    print('ALex')


#print_name = start_end_decorator(print_name)

print_name()


@start_end_decorator
def add5(x):
    return x+5


# TypeError: wrapper() takes 0 positional arguments but 1 was given
result = add5(10)
print(result)  # prints none

print(help(add5))
print(add5.__name__)

########
# template for the decorator


def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # DO....
        result = func(*args, **kwargs)
        # DO....
        return result
    return wrapper
