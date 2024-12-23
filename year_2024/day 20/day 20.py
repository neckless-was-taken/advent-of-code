input = 'year_2024/day 20/example.txt'
# input = 'aoc-inputs/year_2024/day 20/input.txt'

from collections import deque
from functools import cache

# BFS method from: https://stackoverflow.com/questions/77539424/breadth-first-search-bfs-in-python-for-path-traversed-and-shortest-path-taken
@cache
def bfs(graph, node, target):
    visited = {}
    queue = deque()

    visited[node] = None
    queue.append(node)

    while queue:
        m = queue.popleft()
        if m == target:
            path = []
            while m:
                path.append(m)
                m = visited[m]
            return len(path)-1
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited[neighbour] = m
                queue.append(neighbour)
# end


grid = []
for r, line in enumerate(open(input).readlines()):
    line = str(line.strip('\n'))
    row = []
    for c, ch in enumerate(line):
        row.append(ch)
        if ch.lower() == 's':
            start = (r,c)
        if ch.lower() == 'e':
            end = (r,c)
    grid.append(row)

# for i in grid:
#     print(i)

graph = {}

r_max = len(grid)-1
c_max = len(grid[0])-1

for r,row in enumerate(grid):
    for c, col in enumerate(row):
        current = (r,c)
        can_see = []
        if col == '.':
            if r-1 >= 0:
                if grid[r-1][c] == '.':
                    can_see.append((r-1,c))
            if r+1 <= r_max:
                if grid[r+1][c] == '.':
                    can_see.append((r+1,c))
            if c-1 >= 0:
                if grid[r][c-1] == '.':
                    can_see.append((r,c-1))
            if c+1 <= c_max:
                if grid[r][c+1] == '.':
                    can_see.append((r,c+1))
        if can_see:
            graph[current] = can_see

t = bfs(graph, start, end)

print(t)
# for k, v in graph.items():
#     print(k, v)
#     print()

count = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            if c+1 <= c_max:
                c += 1
                can_see = []
                if r-1 >= 0:
                    if grid[r-1][c] == '.':
                        can_see.append((r-1,c))
                if r+1 <= r_max:
                    if grid[r+1][c] == '.':
                        can_see.append((r+1,c))
                if c-1 >= 0:
                    if grid[r][c-1] == '.':
                        can_see.append((r,c-1))
                if c+1 <= c_max:
                    if grid[r][c+1] == '.':
                        can_see.append((r,c+1))
                current = (r,c)
                if can_see:
                    graph[current] = can_see
                c -= 1

            if r+1 <= r_max:
                r += 1
                can_see = []
                if r-1 >= 0:
                    if grid[r-1][c] == '.':
                        can_see.append((r-1,c))
                if r+1 <= r_max:
                    if grid[r+1][c] == '.':
                        can_see.append((r+1,c))
                if c-1 >= 0:
                    if grid[r][c-1] == '.':
                        can_see.append((r,c-1))
                if c+1 <= c_max:
                    if grid[r][c+1] == '.':
                        can_see.append((r,c+1))
                current = (r,c)
                if can_see:
                    graph[current] = can_see
                r -= 1

            if c-1 >= 0:
                c -= 1
                can_see = []
                if r-1 >= 0:
                    if grid[r-1][c] == '.':
                        can_see.append((r-1,c))
                if r+1 <= r_max:
                    if grid[r+1][c] == '.':
                        can_see.append((r+1,c))
                if c-1 >= 0:
                    if grid[r][c-1] == '.':
                        can_see.append((r,c-1))
                if c+1 <= c_max:
                    if grid[r][c+1] == '.':
                        can_see.append((r,c+1))
                current = (r,c)
                if can_see:
                    graph[current] = can_see
                c += 1

            if r-1 >= 0:
                r -= 1
                can_see = []
                if r-1 >= 0:
                    if grid[r-1][c] == '.':
                        can_see.append((r-1,c))
                if r+1 <= r_max:
                    if grid[r+1][c] == '.':
                        can_see.append((r+1,c))
                if c-1 >= 0:
                    if grid[r][c-1] == '.':
                        can_see.append((r,c-1))
                if c+1 <= c_max:
                    if grid[r][c+1] == '.':
                        can_see.append((r,c+1))
                current = (r,c)
                if can_see:
                    graph[current] = can_see
                r += 1
        
        # if bfs(graph, start, end) <= target:
        #     count += 1

# print(count)