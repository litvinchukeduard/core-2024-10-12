from time import time
from functools import wraps
'''
Написати декоратор, який буде рахувати час виконання функції
'''

def timing_decorator(func):
    # def wrapper(*args, **kwargs):
    @wraps(func)
    def wrapper(numbers):
        start_time = time()
        result = func(numbers)
        end_time = time()
        print("Function running time:")
        print((end_time - start_time) * 10000)
        return result
    return wrapper

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@timing_decorator
def count_sum(numbers: list[int]) -> int:
    '''Function to count a sum of numbers'''
    return sum(numbers)

# start_time = time()
# print(count_sum(numbers))

print(count_sum.__doc__)
print(count_sum.__name__)
# end_time = time()

# print((end_time - start_time) * 10000)
