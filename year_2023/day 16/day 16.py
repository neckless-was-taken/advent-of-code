inputFile = 'year_2023/day 16/example.txt'
inputFile = 'aoc-inputs/year_2023/day 16/input.txt'

import time
start_t = time.time()

from collections import deque

def ray_trace(r,c,direction):
    new_map = [['.' for _ in line] for line in input_map]
    q = deque()
    q.append((r,c,direction))
    cache = {}
    while q:
        r, c, direction = q.popleft()
        new_map[r][c] = '#'

        try:
            if direction in cache[(r, c)]:
                continue
            else:
                c_cache = cache[(r,c)]
                c_cache.append(direction)
                cache[(r,c)] = c_cache
        except:
            cache[(r,c)] = [direction]

        if direction == '>':
            if input_map[r][c] in '.-':
                if c < len(input_map[r])-1:
                    q.append((r,c+1,'>'))
                continue
            if input_map[r][c] == '\\':
                if r < len(input_map)-1:
                    q.append((r+1,c,'v'))
                continue
            if input_map[r][c] == '/':
                if r > 0:
                    q.append((r-1,c,'^'))
                continue
            if input_map[r][c] == '|':
                if r > 0:
                    q.append((r-1,c,'^'))
                if r < len(input_map)-1:
                    q.append((r+1,c,'v'))
                continue


        if direction == '<':
            if input_map[r][c] in '.-':
                if c > 0:
                    q.append((r,c-1,'<'))
                continue
            if input_map[r][c] == '\\':
                if r > 0:
                    q.append((r-1,c,'^'))
                continue
            if input_map[r][c] == '/':
                if r < len(input_map)-1:
                    q.append((r+1,c,'v'))
                continue
            if input_map[r][c] == '|':
                if r > 0:
                    q.append((r-1,c,'^'))
                if r < len(input_map)-1:
                    q.append((r+1,c,'v'))
                continue


        if direction == 'v':
            if input_map[r][c] in '.|':
                if r < len(input_map)-1:
                    q.append((r+1,c,'v'))
                continue
            if input_map[r][c] == '\\':
                if c < len(input_map[r])-1:
                    q.append((r,c+1,'>'))
                continue
            if input_map[r][c] == '/':
                if c > 0:
                    q.append((r,c-1,'<'))
                continue
            if input_map[r][c] == '-':
                if c > 0:
                    q.append((r,c-1,'<'))
                if c < len(input_map[r])-1:
                    q.append((r,c+1,'>'))
                continue


        if direction == '^':
            if input_map[r][c] in '.|':
                if r > 0:
                    q.append((r-1,c,'^'))
                continue
            if input_map[r][c] == '\\':
                if c > 0:
                    q.append((r,c-1,'<'))
                continue
            if input_map[r][c] == '/':
                if c < len(input_map[r])-1:
                    q.append((r,c+1,'>'))
                continue
            if input_map[r][c] == '-':
                if c > 0:
                    q.append((r,c-1,'<'))
                if c < len(input_map[r])-1:
                    q.append((r,c+1,'>'))
                continue   
    return new_map
input_map = [[ch for ch in line.strip('\n')] for line in open(inputFile,'r').readlines()]
 
configurations = deque()
for i in range(len(input_map)):
    configurations.append((
        i,
        0,
        '>'
        ))
    configurations.append((
        i,
        len(input_map[i])-1,
        '<'
    ))
    configurations.append((
        0,
        i,
        'v'
    ))
    configurations.append((
        len(input_map[i])-1,
        i,
        '^'
    ))

part2_total = 0
while configurations:
    r,c,direction = configurations.popleft()
    energized_total = 0
    new_map = ray_trace(r,c,direction)
    for row in new_map:
        for ch in row:
            if ch == '#':
                energized_total += 1
    if r == c == 0 and direction == '>':
        part1_total = energized_total
        print(f'part 1 answer: {part1_total}')
    if part2_total < energized_total:
        part2_total = energized_total

print(f'part 2 answer: {part2_total}')
end_t = time.time()
print(f'total time: {end_t-start_t}')