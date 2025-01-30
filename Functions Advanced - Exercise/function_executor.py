def func_executor(*args):
    results = []
    for func, func_args in args:
        results.append(f"{func.__name__} - {func(*func_args)}")
    return "\n".join(results)
def sum_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
