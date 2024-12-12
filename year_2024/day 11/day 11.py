# Part 2 solution from: https://www.youtube.com/watch?v=pVfsmQSlVOQ

# input = 'year_2024/day 11/example.txt'
input = 'aoc-inputs/year_2024/day 11/input.txt'

from tqdm import tqdm
from functools import cache

# rules:
# if 0, = 1
# if even amount of digits, split in two (e.g 1234 becomes 12 and 34)
# else x = x * 2024

def blinker3000(rocks):
    new_rocks = []
    rocks = rocks[::-1]
    for r in rocks:
        if r == 0:
            new_rocks.append(1)
            continue
        digit_count = len(str(r))
        if digit_count % 2 == 0:
            new_rocks.append(int(str(r)[0:int(digit_count/2)]))
            new_rocks.append(int(str(r)[int(digit_count/2):]))
            continue
        new_rocks.append(r * 2024)
        continue
    return new_rocks

# not my solution
@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length//2]), steps - 1) + count(int(string[length//2:]), steps - 1)
    return count(stone * 2024, steps - 1)
# end

for line in open(input).readlines():
    stones = list(map(int, (str(line.strip('\n'))).split()))

for i in range(25):
    stones = blinker3000(stones)

print(f'answer to part 1: {len(stones)}')

# part 2
for line in open(input).readlines():
    stones = list(map(int, (str(line.strip('\n'))).split()))

# for i in tqdm(range(75)):
#     stones = blinker3000(stones)

print(f'answer to part 2: {sum(count(stone, 75) for stone in stones)}')