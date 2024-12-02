#! /usr/bin/env python3

# Day 1: Historian Hysteria

import collections, sys
from typing import Tuple


def part1(source: str) -> Tuple[int, list, list]:
    with open(source, 'r') as f:
        lines = f.read().splitlines()
    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    sum = 0
    for l, r in zip(sorted(left), sorted(right)):
        sum += abs(l - r)
    return sum, left, right


def part2(left: list, right: list) -> int:
    counter = collections.Counter(right)
    similarity = 0
    for l in left:
        similarity += l * counter[l]
    return similarity


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <input_file>')
    else:
        sum, left, right = part1(sys.argv[1])
        print(sum)
        print(part2(left, right))