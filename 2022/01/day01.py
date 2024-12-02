# day01.py
# Calorie counting

import sys

def part1(input):
    with open(input) as f:
        reports = list(f)
        if reports[-1] != '\n':
            reports.append('\n')
        try:
            previous = 0
            results = []
            while True:
                p = reports.index('\n', previous)
                report = list(map(int, reports[previous: p]))
                count = sum(report)
                results.append(count)
                previous = p + 1
        except ValueError:
            results.sort(reverse=True)
    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        calories = part1(sys.argv[1])
        print(calories[0])
        print(sum(calories[:3]))
