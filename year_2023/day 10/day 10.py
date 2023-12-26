# this solution is from: https://www.youtube.com/watch?v=r3i3XE9H4uw

from collections import deque

# inputFile = 'year_2023/day 10/example1.txt'
# inputFile = 'year_2023/day 10/example2.txt'
inputFile = 'aoc-inputs/year_2023/day 10/input.txt'

grid = open(inputFile, 'r').read().strip().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            start_point = (r, c)
            break
        else:
            continue
        break

seen = {(start_point[0],start_point[1])}
q = deque([(start_point[0],start_point[1])])

maybe_S = {"|","F","7","J","L","-"}

while q:
    r, c = q.popleft()
    ch = grid[r][c]
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|F7" and (r-1,c) not in seen:
        seen.add((r-1,c))
        q.append((r-1,c))
        if ch == 'S':
            maybe_S &= {"|","J","L"}
    if r < len(grid) and ch in "S|F7" and grid[r+1][c] in "|JL" and (r+1,c) not in seen:
        seen.add((r+1,c))
        q.append((r+1,c))
        if ch == 'S':
            maybe_S &= {"|","F","7"}
    if c > 0 and ch in "S-J7" and grid[r][c-1] in "-FL" and (r,c-1) not in seen:
        seen.add((r,c-1))
        q.append((r,c-1))
        if ch == 'S':
            maybe_S &= {"-","J","7"}
    if c < len(grid[r]) and ch in "S-FL" and grid[r][c+1] in "-J7" and (r,c+1) not in seen:
        seen.add((r,c+1))
        q.append((r,c+1))
        if ch == 'S':
            maybe_S &= {"-","F","L"}

print(f'part 1: {len(seen)//2}')

assert len(maybe_S) == 1
(S,) = maybe_S

grid = [row.replace("S",S) for row in grid]
grid = [''.join(ch if (r,c) in seen else '.' for c, ch in enumerate(row)) for r, row in enumerate(grid)]

outside = set()

# print('\n'.join(grid))

for r, row in enumerate(grid):
    within = False
    up = None
    for c,ch in enumerate(row):
        if ch == '.':
            pass
        elif ch == '|':
            assert up is None
            within = not within
        elif ch == '-':
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else '7'):
                within = not within
            up = None
        else:
            raise RuntimeError('skibidi toilet: {ch}')
        if not within:
            outside.add((r,c))

print(f'part 2: {len(grid)*len(grid[0])-len(outside | seen)}')