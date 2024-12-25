# input = 'year_2024/day 25/example.txt'
input = 'aoc-inputs/year_2024/day 25/input.txt'

from functools import cache

@cache
def key_fitter(k, l):
    for i in range(len(k)):
        if k[i] + l[i] > 5:
            return 0
    return 1

schematics = []
lines = []

for line in open(input).readlines():
    line = str(line.strip('\n'))
    if line == '':
        schematics.append(lines)
        lines = []
    else:
        lines.append(line)
if len(lines) == 7:
    schematics.append(lines)
    lines = []

locks = []
keys = []
pins = [0,0,0,0,0]

key = 0
lock = 0

for sch in schematics:
    if sch[0] == '#####':
        lock = 1
    if sch[0] == '.....':
        key = 1
    for row in sch[1:-1]:
        for i, p in enumerate(row):
            if p == '#':
                pins[i] += 1
    if key:
        keys.append(pins)
    if lock:
        locks.append(pins)
    pins = [0,0,0,0,0]
    key = 0
    lock = 0

answer_1 = 0

for lock in locks:
    lock = tuple(lock)
    for key in keys:
        key = tuple(key)
        answer_1 += key_fitter(key, lock)

print(answer_1)