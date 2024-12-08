import sys
from enum import Enum

def get_file_as_array(file: str):
    file = open(file).read().strip()
    return [list(row) for row in file.splitlines()]

def parse_file(file_path: str):
    file = open(file_path).read().strip()
    map = {}
    lines = file.splitlines()
    for y, l in enumerate(lines):
        for x, char in enumerate(l.strip()):
            if char != '.':
                if char not in map:
                    map[char] = []
                map[char].append((x, y))
    return (map, len(lines[0]), len(lines))


def in_bounds(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def product(pos):
    list = []
    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            if i == j:
                continue
            list.append((pos[i], pos[j]))
    return list




def antinodes_for_list(nodes_pos: [(int, int)], width: int, height: int) -> [(int, int)]:
    nodes = []
    for a, b in product(nodes_pos):
        x1, y1 = a
        x2, y2 = b

        dx = x1 - x2
        dy = y1 - y2

        if in_bounds(x1 + dx, y1 + dy, width, height):
            nodes.append((x1 + dx, y1 + dy))

        if in_bounds(x2 - dx, y2 - dy, width, height):
            nodes.append((x2 - dx, y2 - dy))
    return nodes


def t_frequencies(nodes_pos: [(int, int)], width: int, height: int) -> [(int, int)]:
    nodes = []
    for a, b in product(nodes_pos):
        x1, y1 = a
        x2, y2 = b

        dx = x1 - x2
        dy = y1 - y2
        nb_nodes = 0
        while in_bounds(x1 + nb_nodes * dx, y1 + nb_nodes * dy, width, height):
            nodes.append((x1 + nb_nodes * dx, y1 + nb_nodes * dy))
            nb_nodes+=1
        nb_nodes =0 
        while in_bounds(x2 - nb_nodes * dx, y2 - nb_nodes * dy, width, height):
            nodes.append((x2 - nb_nodes * dx, y2 - nb_nodes * dy))
            nb_nodes+=1
    return nodes

def solve_first(pos: dict[chr, [(int, int)]], width, height):
    antinodes = []
    for nodes in pos.values():
        antinodes += antinodes_for_list(nodes, width, height)
    return antinodes


def solve_first(pos: dict[chr, [(int, int)]], width, height):
    antinodes = []
    for nodes in pos.values():
        antinodes += t_frequencies(nodes, width, height)
    return antinodes


map, width, height = parse_file(sys.argv[1])
print(f"map={map}\nwidth={width} height={height}")
positions = set(solve_first(map, width, height))

arr = get_file_as_array(sys.argv[1])
for a, b in positions:
    if arr[b][a] == '.':
        arr[b][a] = '#'

for row in arr:
    print("".join(row))
print(len(positions))
