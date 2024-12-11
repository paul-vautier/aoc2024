import sys
from functools import reduce, cache
from math import log10, floor


def nb_digits(num):
    return floor(log10(num))+1


def parse_file(file_path: str):
    file = open(file_path).read().strip()
    return list(map(int, file.split(" ")))


@cache
def transform(current, iterations):
    if iterations == 0:
        return 1
    if current == 0:
        return transform(1, iterations - 1)
    else:
        digits_current = nb_digits(current)
        if digits_current % 2 == 0:
            split = 10**(digits_current / 2)
            return transform(int(current//split), iterations - 1) + transform(int(current % split), iterations - 1)
        else:
            return transform(current*2024, iterations - 1)


def solve_first(input: [int]) -> int:
    total = 0
    for i in input:
        total += transform(i, 25)
    return total


def solve_second(input: [int]) -> int:
    total = 0
    for i in input:
        total += transform(i, 75)
    return total


print(solve_first(parse_file(sys.argv[1])))
print(solve_second(parse_file(sys.argv[1])))
