inputFile = 'year_2023/day 21/example.txt'
# inputFile = 'aoc-inputs/year_2023/day 21/input.txt'

import time
start_t = time.time()

from collections import deque

input_map = []
for r, line in enumerate(open(inputFile).readlines()):
    new_line = []
    for c, ch in enumerate(line.strip('\n')):
        new_line.append(ch)
        if ch == 'S':
            start = (r, c, 0)
    input_map.append(new_line)

step_count = 6
seen = set()
q = deque()
q.append(start)

while q:
    r, c, step = q.popleft()



end_t = time.time()
print(f'total time: {end_t-start_t}')