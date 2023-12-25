# this solution is from : https://www.youtube.com/watch?v=guOyA7Ijqgk

# inputFile = 'year_2023/day 24/example.txt'
inputFile = 'aoc-inputs/year_2023/day 24/input.txt'

import time

start_time = time.time()

import sympy

hailstones = [tuple(map(int, line.replace('@',',').split(','))) for line in open(inputFile, 'r').readlines()]

total = 0

lower = 7
upper = 27
lower = 200000000000000
upper = 400000000000000

print('ha')

for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[:i]:
        px, py = sympy.symbols("px py")
        answers = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [hs1, hs2]])
        if answers == []:
            continue
        x, y = answers[px], answers[py]
        if lower <= x <= upper and lower <= y <= upper:
            if all((x - sx) * vx and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [hs1, hs2]):
                total += 1

print(total)

end_time = time.time()

print(f"Elapsed time: {end_time - start_time} seconds")