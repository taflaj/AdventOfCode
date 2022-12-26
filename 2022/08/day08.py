# day08.py
# Treetop tree house

import sys

def part1(data: list, width: int, height: int) -> int:
    outer = (width + height - 2) * 2
    inner = 0
    for y in range(1, height - 1):
        row = data[y]
        for x in range(1, width - 1):
            tree = row[x]
            left = [n for n in row[0:x] if n >= tree]
            if len(left) > 0:
                right = [n for n in row[x+1:width] if n >= tree]
                if len(right) > 0:
                    column = [data[row][x] for row in range(height)]
                    above = [n for n in column[0:y] if n >= tree]
                    if len(above) > 0:
                        below = [n for n in column[y+1:height] if n >= tree]
                        if len(below) > 0:
                            continue
            inner += 1
    return outer + inner

def get_score(tree: str, side: list) -> int:
    score = 0
    for height in side:
        score += 1
        if height >= tree:
            break
    return score

def part2(data: list, width: int, height: int) -> int:
    score = 0
    for y in range(1, height - 1):
        row = data[y]
        for x in range(1, width - 1):
            tree = row[x]
            left = get_score(tree, list(row[0:x][::-1]))
            right = get_score(tree, list(row[x+1:width]))
            column = [data[row][x] for row in range(height)]
            above = get_score(tree, [n for n in reversed(column[0:y])])
            below = get_score(tree, [n for n in column[y+1:height]])
            score = max(score, left * right * above * below)
    return score

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        file = sys.argv[1]
        with open(file) as f:
            data = f.read().splitlines()
        width = len(data[0])
        height = len(data)
        print(part1(data, width, height))
        print(part2(data, width, height))