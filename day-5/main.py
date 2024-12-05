import sys
from typing import *


def solve_first(orderings: dict[set[int]], rules: [int]):
    middles = []
    for rule in rules.strip().split('\n'):
        nums = list(map(int, rule.split(',')))
        ok = True
        seen = []
        for num in nums:
            seen.append(num)
            if not ok:
                break
            for num_before in ordering_map.get(num, []):
                if num_before not in seen and num_before in nums:
                    ok = False
                    break
        if ok:
            middles.append(nums[int(len(nums)/2)])

    return sum(middles)


def index_of(L, obj):
    for i, el in enumerate(L):
        if el == obj:
            return i
    return -1


def solve_second(orderings: dict[set[int]], rules: [int]):

    middles = []
    for rule in rules.strip().split('\n'):
        nums = list(map(int, rule.split(',')))
        ok = True
        index = 0
        while index < len(nums):
            permut = False
            for num_before in ordering_map.get(nums[index], []):
                idx_before = index_of(nums, num_before)
                if idx_before != -1 and idx_before > index:
                    ok = False
                    permut = True
                    tmp = nums[index]
                    nums[index] = num_before
                    nums[idx_before] = tmp
            if not permut:
                index += 1

        if not ok:
            middles.append(nums[int(len(nums)/2)])

    return sum(middles)


with open(sys.argv[1]) as file:
    orderings, rules = file.read().split('\n\n')

    ordering_map = {}

    for ordering in orderings.split('\n'):
        first, second = map(int, ordering.split('|'))

        if second not in ordering_map:
            ordering_map[second] = set()
        ordering_map[second].add(first)
    print(solve_first(orderings, rules))
    print(solve_second(orderings, rules))
