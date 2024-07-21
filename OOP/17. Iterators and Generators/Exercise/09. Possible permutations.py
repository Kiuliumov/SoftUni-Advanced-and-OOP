import itertools


def possible_permutations(iterable):
    for permutation in itertools.permutations(iterable):
        yield permutation
