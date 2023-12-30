# inputFile = 'year_2023/day 14/example.txt'
inputFile = 'aoc-inputs/year_2023/day 14/input.txt'

from tqdm import tqdm

grid = list(zip(*[[ch for ch in line.strip('\n')] for line in open(inputFile).readlines()]))


# for i in grid:
#     print(i)

def rock_slider_3000(grid):

    def roll(sr, er, x):
        x[sr] = '.'
        x[er] = 'O'
        return x
    
    new_grid = []
    for r, row in enumerate(grid):
        row = list(row)
        new_row = []
        can_roll = False
        end_roll = 0
        start_roll = 0
        for c, ch in enumerate(row):
            if ch != '.' and c <= len(row)-1:
                if ch == '#':
                    can_roll = False
                    end_roll = c
                if ch == 'O' and can_roll:
                    start_roll = c
                    if start_roll > end_roll:
                        new_row = roll(start_roll, end_roll, list(row[:c+1]))
                        for e, i in enumerate(new_row):
                            row[e] = str(i)
                        if start_roll - end_roll > 1:
                            can_roll = True
                        else:
                            can_roll = False
                end_roll += 1
            elif ch == '.':
                can_roll = True

        new_grid.append(row)
    return list(zip(*new_grid))

total = 0

part1_grid = rock_slider_3000(grid)
print(sum(row.count("O") * (len(part1_grid) - i) for i, row in enumerate(part1_grid)))