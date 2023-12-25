# this solution is from : https://www.youtube.com/watch?v=guOyA7Ijqgk

# inputFile = 'year_2023/day 24/example.txt'
inputFile = 'aoc-inputs/year_2023/day 24/input.txt'

class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = int(sx)
        self.sy = int(sy)
        self.sz = int(sz)
        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)

        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy

    def __repr__(self):
        pass

hailstones = [Hailstone(*map(int, line.replace('@',',').split(','))) for line in open(inputFile, 'r').readlines()]

total = 0

lower = 7
upper = 27
lower = 200000000000000
upper = 400000000000000

for i, hs1 in enumerate(hailstones):
    for hs2 in hailstones[:i]:
        a1,b1,c1 = hs1.a, hs1.b, hs1.c
        a2,b2,c2 = hs2.a, hs2.b, hs2.c
        if a1 * b2 == a2 * b1:
            continue
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        if lower <= x <= upper and lower <= y <= upper:
            if all((x - hs.sx) / hs.vx and (y - hs.sy) / hs.vy >= 0 for hs in (hs1, hs2)):
                total += 1

print(total)