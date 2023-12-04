from collections import deque

# input = 'year_2022/day 12/example.txt'
input = 'aoc-inputs/year_2022/day 12/input.txt'

map = [list(line.strip('\n')) for line in open(input,'r').readlines()]

start_index = ['']
end_index = ['']
steps = []
step_c = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

spl = []

for row in range(0,len(map)):
    try:
        start_index.append(map[row].index('S'))
        start_index[0] = row
        map[start_index[0]][start_index[1]] = 'a'
    except:
        pass
    try:
        end_index.append(map[row].index('E'))
        end_index[0] = row
        map[end_index[0]][end_index[1]] = 'z'
    except:
        pass
    for col in range(0,len(map[row])):
        if map[row][col] == 'a':
            spl.append([row,col])
        map[row][col] = alphabet.index(map[row][col])

print('starting index :',start_index)
print('end index :',end_index)

current_index = start_index

paths = []

for sp in spl:
    vis = {(sp[0],sp[1])}
    q = deque()
    q.append((0, sp[0],sp[1]))
    #print(q)
    while q:
        d, r, c = q.popleft()
        for nr, nc in [(r+1, c),(r-1,c),(r,c+1),(r,c-1)]:
            if nr < 0 or nc < 0 or nr >= len(map) or nc >= len(map[0]):
                continue
            if (nr, nc) in vis:
                continue
            if map[nr][nc] - map[r][c] > 1:
                continue
            if nr == end_index[0] and nc == end_index[1]:
                paths.append(d+1)
                break
            vis.add((nr,nc))
            q.append((d+1,nr,nc))

print(min(paths))

# print('step count :',step_c)
# print('last index :',current_index)