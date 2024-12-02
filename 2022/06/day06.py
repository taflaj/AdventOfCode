# day06.py
# Tuning trouble

import sys

def part1(sequence: str, size: int) -> int:
    for i in range(len(sequence) - size):
        unique = set(sequence[i : i + size])
        if len(unique) == size:
            return i + size
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        file = sys.argv[1]
        with open(file) as f:
            sequence = f.readline()
        print(part1(sequence, 4))
        print(part1(sequence, 14))