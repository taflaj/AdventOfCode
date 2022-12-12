# RockPaperScissors.py

import sys

def part1(input: str) -> list:
    awards = {'X': 1, 'Y': 2, 'Z': 3}
    with open(input) as f:
        rounds = list(f)
        points = 0
        for round in rounds:
            elf = round[0]
            me = round[-2]
            match = [elf, me]
            outcome = 0
            if match == ['A', 'X'] or match == ['B', 'Y'] or match == ['C', 'Z']:
                outcome = 3
            elif match == ['A', 'Y'] or match == ['B', 'Z'] or match == ['C', 'X']:
                outcome = 6
            points += outcome + awards[me]
        print(points)
    return rounds

def part2(rounds: list) -> int:
    points = 0
    outcomes = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
    for round in rounds:
        elf = round[0]
        me = round[-2]
        points += outcomes[elf + me]
    return points

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        rounds = part1(sys.argv[1])
        print(part2(rounds))