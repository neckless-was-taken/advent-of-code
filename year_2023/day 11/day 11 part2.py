# this solution is from: https://www.youtube.com/watch?v=3DFhqYVF9AM

# inputFile = 'year_2023/day 11/example.txt'
inputFile = 'aoc-inputs/year_2023/day 11/input.txt'

def solver(points,empty_rows,empty_cols,scale):
    total = 0
    for i, (r1, c1) in enumerate(points):
        for (r2, c2) in points[:i]:
            for r in range(min(r1, r2),max(r1,r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1,c2),max(c1,c2)):
                total += scale if c in empty_cols else 1
    return total

grid = open(inputFile, 'r').read().strip().splitlines()

empty_rows = [r for r, row in enumerate(grid) if all(ch == '.' for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == '.' for ch in col)]

points = [(r,c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '#']

print(f'part 1: {solver(points,empty_rows,empty_cols,2)}')
print(f'part 2: {solver(points,empty_rows,empty_cols,1000000)}')