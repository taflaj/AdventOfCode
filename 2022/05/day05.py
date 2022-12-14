# day05.py
# Supply stacks

import sys

def part1(stacks: list, file: str) -> list:
    with open(file) as f:
        contents = f.read().splitlines()
    commands = [line.split(' ') for line in contents if line.startswith('move')]
    for command in commands:
        quantity = int(command[1])
        source = stacks[int(command[3]) - 1]
        target = stacks[int(command[5]) - 1]
        for _i in range(quantity):
            target.append(source.pop())
    print([stacks[i][-1] for i in range(len(stacks))])
    return commands

def part2(stacks: list, commands: list) -> None:
    for command in commands:
        quantity = int(command[1])
        source = stacks[int(command[3]) - 1]
        target = stacks[int(command[5]) - 1]
        n = len(source) - quantity
        shift = source[n:]
        del source[n:]
        target += shift
    print([stacks[i][-1] for i in range(len(stacks))])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        file = sys.argv[1]
        data = ['DBJV', 'PVBWRDF', 'RGFLDCWQ', 'WJPMLNDB', 'HNBPCSQ', 'RDBSNG', 'ZBPMQFSH', 'WLF', 'SVFMR'] if file == 'input.txt' else ['ZN', 'MCD', 'P']
        # I don't know why list copying isn't working here
        commands = part1([[st for st in data[i]] for i in range(len(data))], file)
        part2([[st for st in data[i]] for i in range(len(data))], commands)
