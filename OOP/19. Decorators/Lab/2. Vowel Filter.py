from typing import Callable


def vowel_filter(function: Callable):
    def wrapper():

        func_list: list = function()
        return_list: list = []

        for letter in func_list:
            if letter in 'aouei':
                return_list.append(letter)
        return return_list

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
