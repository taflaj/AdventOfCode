# day07.py
# No space left on device

import sys
from typing import Tuple


class Folder:
    def __init__(self, parent: 'Folder'=None) -> None:
        super().__init__()
        self.parent = parent
        self.size = 0
        self.files = {}
        self.folders = {}

    def print(self, depth: int=0) -> None:
        print(f'{"= " * depth}{self.size}')
        for name, size in self.files.items():
            print(f'{"- " * depth}{name} {size}')
        for name, folder in self.folders.items():
            print(f'{"+ " * depth}{name}:')
            folder.print(depth + 1)
        
    def add_file(self, name: str, size: int) -> 'Folder':
        self.files[name] = size
        return self

    def add_folder(self, name: str) -> 'Folder':
        folder = Folder(self)
        self.folders[name] = folder
        return folder

    def sum(self) -> int:
        self.size = sum(self.files.values()) + sum([folder.sum() for folder in self.folders.values()])
        return self.size


def part1(input: str) -> Tuple[list, int]:
    root = Folder()
    with open(input) as f:
        contents = [line.split(' ') for line in f.read().splitlines()]
    current = root
    folders = []
    for line in contents:
        if line[0] == '$':
            if line[1] == 'cd':
                target = line[2]
                if target == '..':
                    current = current.parent
                elif target == '/':
                    current = root
                else:
                    current = current.folders[target]
        else:
            name = line[1]
            if line[0] == 'dir':
                folders.append(current.add_folder(name))
            else:
                current.add_file(name, int(line[0]))
    root.sum()
    sizes = [folder.size for folder in folders]
    return sorted(sizes), root.size
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
    else:
        sizes, total = part1(sys.argv[1])
        print(sum([size for size in sizes if size < 100_000]))
        free = 70_000_000 - total
        needed = 30_000_000 - free
        candidates = [size for size in sizes if size >= needed]
        print(candidates[0])