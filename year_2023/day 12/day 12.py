# this solution is from: https://www.youtube.com/watch?v=g3Ms5e7Jdqo

# inputFile = 'year_2023/day 12/example.txt'
inputFile = 'aoc-inputs/year_2023/day 12/input.txt'


def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0 
    if nums == ():
        return 0 if '#' in cfg else 1
    
    result = 0

    key = (cfg, nums)

    if key in cache:
        return cache[key]
    else:
        if cfg[0] in '.?':
            result += count(cfg[1:],nums)

        if cfg[0] in '?#':
            if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
                result += count(cfg[nums[0]+1:],nums[1:])
        cache[key] = result
        return result

grid = open(inputFile, 'r').read().strip().splitlines()

cache = {}
total = 0

for line in open(inputFile):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(',')))

    total += count(cfg,nums)
print(f'part 1: {total}')

cache = {}
total = 0

for line in open(inputFile):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(',')))

    cfg = '?'.join([cfg]*5)
    nums *= 5

    total += count(cfg,nums)

print(f'part 2: {total}')