# revisit date: 27/12/2023

inputFile = 'year_2022/day 3/example.txt'
inputFile = 'aoc-inputs/year_2022/day 3/input.txt'

alphabet=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

total = 0
for line in open(inputFile).readlines():
    for ch in line.strip('\n'):
        if ch in line[(len(line)//2):]:
            total += alphabet.index(ch)+1
            break
print(f'part 1: {total}')

elf = []
total = 0
for line in open(inputFile).readlines():
    elf.append(line.strip('\n'))
    if len(elf) == 3:
        for ch in elf[0]:
            if ch in elf[1] and ch in elf[2]:
                total += alphabet.index(ch)+1
                elf = []
                break
print(f'part 2: {total}')