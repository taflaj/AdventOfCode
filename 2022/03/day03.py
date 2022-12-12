# day03.py
# Rucksack reorganization

import sys

def priority(input: str) -> int:
    result = ord(input) - ord('a') + 1
    if result < 0:
        result += 58
    return result


def part1(input: str) -> list:
    total = 0
    with open(input) as f:
        contents = f.read().split('\n')
        if contents[-1] == '':
            contents.pop()
        for rucksack in contents:
            l = len(rucksack) // 2
            repeated = set(rucksack[:l]) & set(rucksack[l:])
            total += priority(repeated.pop())
    print(total)
    return contents

def part2(input: list) -> None:
    total = 0
    while len(input) > 0:
        badge = set(input.pop()) & set(input.pop()) & set(input.pop())
        total += priority(badge.pop())
    print(total)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        contents = part1(sys.argv[1])
        part2(contents)