def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == "even":
        return [num for num in numbers if num % 2 == 0]
    elif command == "odd":
        return [num for num in numbers if num % 2 != 0]
print(even_odd(1, 2, 3, 4, 5, 6, "even"))  # Output: [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))  # Output: [1, 3, 5, 7, 9]
