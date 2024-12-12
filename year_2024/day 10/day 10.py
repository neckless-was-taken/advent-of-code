# input = 'year_2024/day 10/example.txt'
input = 'aoc-inputs/year_2024/day 10/input.txt'

from collections import deque

grid = []

trail_heads = []

for r, line in enumerate(open(input).readlines()):
    line = str(line.strip('\n'))
    row = []
    for c, x in enumerate(line):
        x = int(x)
        if x == 0:
            trail_heads.append([r,c])
        row.append(x)

    grid.append(row)

emax = len(grid[0])-1
smax = len(grid)-1

count = 0

part_1_count = 0

for head in trail_heads:
    part_1 = []
    r, c = head[0], head[1]
    h = 0
    q = deque()
    q.append([r,c,h])
    while q:
        r, c, h = q.popleft()
        if h == 9:
            if [r,c,h] not in part_1:
                part_1.append([r,c,h])
            count += 1
            continue
        if r - 1 >= 0:
            if grid[r-1][c] == h+1:
                q.append([r-1, c, h+1])
        if c+1 <= emax:
            if grid[r][c+1] == h+1:
                q.append([r, c+1, h+1])
        if r+1 <= smax:
            if grid[r+1][c] == h+1:
                q.append([r+1, c, h+1])
        if c-1 >= 0:
            if grid[r][c-1] == h+1:
                q.append([r, c-1, h+1])
    part_1_count += len(part_1)

print(f'answer to part 1: {part_1_count}')
print(f'answer to part 2: {count}')

# part 1 is very confusing. I found the solution for part 2 when solving part 1 and had to add a janky way of solving part 1