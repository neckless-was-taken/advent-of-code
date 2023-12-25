# inputFile = 'year_2023/day 9/example.txt'
inputFile = 'aoc-inputs/year_2023/day 9/input.txt'

def allZeroes(lst):
    return all(element == 0 for element in lst)

inputs = [list(*[map(int, ranges.split()) for ranges in line.splitlines()]) for line in open(inputFile).readlines()]

total = 0

for history in inputs:
    difference = []
    x = []
    new_values = []
    for e, value in enumerate(history):
        if e == 0:
            continue
        x.append(value-history[e-1])
    difference.append(x)
    while not allZeroes(difference[-1]):
        x = []
        for e, i in enumerate(difference[-1]):
            if e == 0:
                continue
            x.append(i-difference[-1][e-1])
        difference.append(x)
    # print(difference)
    for e, i in enumerate(reversed(difference)):
        if e < 2:
            new_values.append(i[-1]+(i[-1]-i[-2]))
            continue
        new_values.append(i[-1]+new_values[-1])
    total += history[-1]+new_values[-1]
print(total)