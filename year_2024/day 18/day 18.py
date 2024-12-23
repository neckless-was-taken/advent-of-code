input = 'year_2024/day 18/example.txt'
size = 6
memory = 12
input = 'aoc-inputs/year_2024/day 18/input.txt'
size = 70
memory = 1024

size += 1

from collections import deque

# BFS method from: https://stackoverflow.com/questions/77539424/breadth-first-search-bfs-in-python-for-path-traversed-and-shortest-path-taken
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
            return path[::-1]
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited[neighbour] = m
                queue.append(neighbour)
    return 0
# end 

grid = []
for r in range(size):
    row = []
    for c in range(size):
        row.append('.')
    grid.append(row)

byte_list = []

for e,line in enumerate(open(input).readlines()):
    if e < memory:
        line = str(line.strip('\n'))
        byte = list(map(int,line.split(',')))
        grid[byte[1]][byte[0]] = '#'
    else:
        line = str(line.strip('\n'))
        byte = list(map(int,line.split(',')))
        byte_list.append(byte)

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
        
        graph[current] = can_see

start = (0,0)
end = (len(grid)-1, len(grid[0])-1)

path = bfs(graph, start, end)

print(f'answer to part 1: {len(path)-1}')

for b in byte_list:
    c = b[0] # current col
    r = b[1] # current row
    grid[r][c] = '#'
    # print(f'updated memory row: {r} and col: {c}')

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
        # print(f'previous graph[{current}] = {graph[current]}')
        graph[current] = can_see
        # print(f'updated graph[{current}] = {graph[current]}')
        r += 1

    # print()
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
        # print(f'previous graph[{current}] = {graph[current]}')
        graph[current] = can_see
        # print(f'updated graph[{current}] = {graph[current]}')
        c += 1

    # print()
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
        # print(f'previous graph[{current}] = {graph[current]}')
        graph[current] = can_see
        # print(f'updated graph[{current}] = {graph[current]}')

        r -= 1
    # print()
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
        # print(f'previous graph[{current}] = {graph[current]}')
        graph[current] = can_see
        # print(f'updated graph[{current}] = {graph[current]}')
        c -= 1

    # print()
    if bfs(graph, start, end) == 0:
        print(f'answer to part 2: {c},{r}')
        break