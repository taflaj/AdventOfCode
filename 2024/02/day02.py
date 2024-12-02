#! /usr/bin/env python3

# Day 2: Red-Nosed Reports

import sys
from typing import Tuple


def is_safe(report: list) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return all(difference >= 1 and difference <= 3 for difference in differences) \
    or all(difference <= -1 and difference >= -3 for difference in differences)


def part1(source: str) -> Tuple[int, list]:
    with open(source, 'r') as f:
        lines = f.read().splitlines()
    safe = 0
    maybe = []
    for line in lines:
        report = [int(level) for level in line.split()]
        if is_safe(report):
            safe += 1
        else:
            maybe.append(report)
    return safe, maybe


def part2(maybe: list) -> int:
    safe = 0
    for report in maybe:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                safe += 1
                break
    return safe


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <input_file>')
    else:
        safe, maybe = part1(sys.argv[1])
        print(safe)
        print(safe + part2(maybe))