import sys
from math import log10, floor
from enum import Enum


def parse_file(file_path: str):
    file = open(file_path).read().strip()
    res = []
    for line in file.splitlines():
        target, nums = line.split(": ")
        nums = list(map(int, nums.split(" ")))
        res.append((int(target), nums))
    return res


def dfs(target: int, current: int, nums: [int]) -> bool:
    if current == target and not nums:
        return True
    if not nums:
        return False
    if target < current:
        return False

    return dfs(target, current + nums[0], nums[1:]) or dfs(target, current * nums[0], nums[1:])


def concat(a: int, b: int):
    return 10 ** (floor(log10(b))+1) * a + b


def dfs_2(target: int, current: int, nums: [int]) -> bool:
    if current == target and not nums:
        return True
    if not nums:
        return False
    if target < current:
        return False

    return dfs_2(target, current + nums[0], nums[1:]) \
        or dfs_2(target, current * nums[0], nums[1:]) \
        or dfs_2(target, concat(current, nums[0]), nums[1:])


def solve_first(targets: [(int, [int])]) -> int:
    return sum(list(map(lambda x: x[0], filter(lambda t: dfs(t[0], t[1][0], t[1][1:]), targets))))


def solve_second(targets: [(int, [int])]) -> int:
    return sum(list(map(lambda x: x[0], filter(lambda t: dfs_2(t[0], t[1][0], t[1][1:]), targets))))


print(solve_first(parse_file(sys.argv[1])))
print(solve_second(parse_file(sys.argv[1])))
