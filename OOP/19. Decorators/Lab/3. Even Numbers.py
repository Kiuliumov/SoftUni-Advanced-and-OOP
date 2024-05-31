from typing import Callable


def even_numbers(function: Callable):

    def wrapper(numbers: list):
        even_numbers: list = []

        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)

        return even_numbers

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))