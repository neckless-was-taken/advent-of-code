# this solution is from: https://www.youtube.com/watch?v=GYbjIvTQ_HA

def find_mirror(grid):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a,b in zip(x,y)) for x,y in zip(above, below)) == 1:
            return r
    return 0

# inputFile = 'year_2023/day 13/example.txt'
inputFile = 'aoc-inputs/year_2023/day 13/input.txt'

total = 0

for block in open(inputFile).read().split('\n\n'):
    grid = block.splitlines()

    total += find_mirror(grid) * 100
    total += find_mirror(list(zip(*grid)))

print(total)
