from collections import deque

# inputFile = 'year_2023/day 11/example.txt'
inputFile = 'aoc-inputs/year_2023/day 11/input.txt'

def visited_pair(a,b,visited):
    return (a,b) in visited or (b,a) in visited

def expansion(grid):
    def expand(grid_to_expand):
        empty = ""
        for dot in range(0,len(grid)):
            empty += '.'
        new_grid = []
        for row in grid_to_expand:
            if all(ch == '.' for ch in row):
                new_grid.extend([row,empty])
            else:
                new_grid.append(row)
        return new_grid
    grid = expand(grid)
    grid = expand([''.join(map(str, row)) for row in zip(*grid)])
    return [''.join(map(str, row)) for row in zip(*grid)]

grid = expansion(open(inputFile, 'r').read().strip().splitlines())

# print('\n'.join(grid))

visited = set()
galaxies = []

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            galaxies.append((r,c))

q = deque((a,b) for a in galaxies for b in galaxies[:galaxies.index(a)])

total = 0

while q:
    a, b = q.popleft()
    x, y = abs(a[0]-b[0]), abs(a[1]-b[1])
    if not visited_pair(x,y,visited):
        visited.add((a,b))
        total += x + y

print(total)
