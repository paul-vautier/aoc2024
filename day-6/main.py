import sys
from enum import Enum


def get_file_as_array(file: str):
    file = open(file).read().strip()
    return [list(row) for row in file.splitlines()]

# ((pos), {walls}, (bounds))


def parse_file(file_path: str) -> ((int, int), {(int, int)}):
    file = open(file_path).read()
    walls = set()
    start_pos = (-1, -1)
    lines = file.split('\n')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '^':
                start_pos = (x, y)
    return (start_pos, get_file_as_array(file_path), (len(lines[0]), len(lines)-1))


directions = [
    (0, -1), (1, 0), (0, 1), (-1, 0)
]


def solve_first(pos: (int, int), map: [[int]], bx: int, by: int):
    visited = set()
    visited.add(pos)

    direction_idx = 0
    dx, dy = directions[direction_idx]
    x, y = pos
    while True:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= bx or ny < 0 or ny >= by:
            visited.add((x, y))
            break
        if map[ny][nx] == '#':
            direction_idx = (direction_idx + 1) % 4
            dx, dy = directions[direction_idx]
        else:
            visited.add((x, y))
            x, y = nx, ny

    return visited


def solve_second(pos: (int, int), map: [[int]], bx: int, by: int):
    visited = set()
    loop = set()
    visited.add(pos)

    direction_idx = 0
    dx, dy = directions[direction_idx]
    x, y = pos
    while True:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= bx or ny < 0 or ny >= by:
            break
        if map[ny][nx] == '#':
            direction_idx = (direction_idx + 1) % 4
            dx, dy = directions[direction_idx]
        else:
            if (x, y, direction_idx) in loop:
                return True
            loop.add((x, y, direction_idx))
            x, y = nx, ny

    return False


pos, walls, bounds = parse_file(sys.argv[1])
visited = solve_first(pos, walls, bounds[0], bounds[1])

print(len(visited))
cnt = 0

for (x, y) in visited:
    if walls[y][x] != "#":
        walls[y][x] = "#"
        if solve_second(pos, walls, bounds[0], bounds[1]):
            cnt += 1
        walls[y][x] = "."

print(cnt)
