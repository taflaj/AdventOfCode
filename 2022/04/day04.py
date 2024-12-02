# day04.py
# Camp cleanup

import sys

def part1(input: str) -> list:
    total = 0
    pairs = []
    with open(input) as f:
        contents = f.read().split('\n')
        if contents[-1] == '':
            contents.pop()
        for pair in contents:
            assignments = pair.split(',')
            left = list(map(int, assignments[0].split('-')))
            right = list(map(int, assignments[1].split('-')))
            pairs.append([left, right])
            if (left[0] <= right[0] and left[1] >= right[1]) \
            or (right[0] <= left[0] and right[1] >= left[1]):
                total += 1
    print(total)
    return pairs

def part2(input: list) -> None:
    total = 0
    for pair in input:
        overlap = set(range(pair[0][0], pair[0][1]+1)) & set(range(pair[1][0], pair[1][1]+1))
        if len(overlap) > 0:
            total += 1
    print(total)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        pairs = part1(sys.argv[1])
        part2(pairs)