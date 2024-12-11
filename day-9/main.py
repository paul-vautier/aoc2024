import sys
from enum import Enum


def get_file_as_array(file: str):
    file = open(file).read().strip()
    return [list(row) for row in file.splitlines()]


def parse_file(file_path: str):
    file = list(map(int, list(open(file_path).read().strip())))
    arr = []
    for i in range(0, len(file)-1, 2):
        idx = i/2
        for full in range(file[i]):
            arr.append(int(idx))
        for empty in range(file[i+1]):
            arr.append(-1)
    for full in range(file[-1]):
        arr.append(int(len(file)/2))
    return arr


def ipt_to_string(ipt):
    return "".join(list(map(lambda x: str(x) if x != -1 else ".", ipt)))


def solve_first(input: [int]):
    start = 0
    end = len(input) - 1
    while start < end:
        if input[start] != -1:
            start += 1
        elif input[end] == -1:
            end -= 1
        else:
            input[start] = input[end]
            input[end] = -1
    sum = 0
    for idx in range(end):
        sum += idx * input[idx]

    return sum


def format_second(input: [int]):
    # Iterate through the parsed list to identify blocks and spans
    blocks = []
    spans = []
    i = 0
    while i < len(input):
        start = i
        size = 1
        current = input[i]

        while i + 1 < len(input) and input[i + 1] == current:
            size += 1
            i += 1

        if current == -1:
            spans.append((start, size))
        else:
            blocks.append((start, size))

        i += 1

    return blocks, spans


def solve_second(input: [int]):
    blocks, spans = format_second(input)

    for block_id, (block_idx, block_size) in reversed(list(enumerate(blocks))):

        offset=0
        for span_idx, (span_start, size) in enumerate(spans):
            if span_start > block_idx:
                break
            if size >= block_size:
                for i in range(span_start, span_start+block_size):
                    input[i] = block_id
                for i in range(block_idx, block_idx+block_size):
                    input[i] = -1
                if size == block_size:
                    spans.pop(span_idx-offset)
                    offset += 1
                else:
                    spans[span_idx-offset] = (span_start+block_size, size - block_size)
                break

    idx = 0
    sum = 0
    for idx, v in enumerate(input):
        if v != -1:
            sum += idx * input[idx]
            idx += 1

    return sum


repr = parse_file(sys.argv[1])

print(solve_first(repr))
repr = parse_file(sys.argv[1])
print(solve_second(repr))
