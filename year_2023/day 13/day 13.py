# inputFile = 'year_2023/day 13/example.txt'
inputFile = 'aoc-inputs/year_2023/day 13/input.txt'

def solver(block):
    for e, line in enumerate(block):
        if e == len(block)-1:
            continue
        if block[e+1] == line:
            if e+1 <= len(block) // 2:
                if block[:e+1] == block[e+e+1:e:-1]:
                    # print(block[:e+1])
                    # print(block[e+e+1:e:-1])
                    return e+1
            elif e+1 > len(block) // 2:
                if block[e-(len(block)-e)+2:e+1] == block[:e:-1]:
                # print('\n'.join(block))
                # print(block[e-(len(block)-e)+2:e+1])
                # print(block[:e:-1])
                    return e+1

    return 0
blocks = []
block = []
for line in open(inputFile).readlines():
    if line == '\n':
        blocks.append(block)
        block = []
    else:
        block.append(line.strip('\n'))
blocks.append(block)
total = 0

for i, block in enumerate(blocks):
    result = 0
    result = solver(block)
    if result:
        total += result * 100
        continue
    result = solver([''.join(map(str, row)) for row in zip(*block)])
    if result:
        total += result
        continue
    raise RuntimeError(i)
print(f'part 1: {total}')