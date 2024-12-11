import sys
from math import log10, floor
from enum import Enum


def parse_file(file_path: str):
    file = open(file_path).read().strip()
    return [list(map(int, row)) for row in file.splitlines()]


directions = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]


def walk_dfs(targets: [[int]], x, y, visited):
    if targets[y][x] == 9 and (x, y) not in visited:
        visited.add((x, y))
        return 1

    total = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if ny >= 0 and ny < len(targets) and nx >= 0 and nx < len(targets[0]):
            if targets[ny][nx] == targets[y][x] + 1:
                total += walk_dfs(targets, nx, ny, visited)

    return total


def walk_dfs_2(targets: [[int]], x, y):
    if targets[y][x] == 9:
        return 1

    total = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if ny >= 0 and ny < len(targets) and nx >= 0 and nx < len(targets[0]):
            if targets[ny][nx] == targets[y][x] + 1:
                total += walk_dfs_2(targets, nx, ny)

    return total


def solve_first(targets: [[int]]) -> int:
    starts = [(x, y) for y, row in enumerate(targets)
              for x, value in enumerate(row) if value == 0]
    return sum(map(lambda start: walk_dfs(targets, start[0], start[1], set()), starts))


def solve_second(targets: [[int]]) -> int:
    starts = [(x, y) for y, row in enumerate(targets)
              for x, value in enumerate(row) if value == 0]
    return sum(map(lambda start: walk_dfs_2(targets, start[0], start[1]), starts))


arr = parse_file(sys.argv[1])

print(solve_first(parse_file(sys.argv[1])))
print(solve_second(parse_file(sys.argv[1])))
