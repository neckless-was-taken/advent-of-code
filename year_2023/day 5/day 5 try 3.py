# this solution is from: https://www.youtube.com/watch?v=NmxHw_bHhGM

# inputFile = 'year_2023/day 5/example1.txt'
inputFile = 'aoc-inputs/year_2023/day 5/input.txt'

seeds, *blocks = open(inputFile).read().split('\n\n')

seeds = list(map(int, seeds.split(':')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if x in range(b, b+c):
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new
print(min(seeds))