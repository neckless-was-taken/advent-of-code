# revisit date: 31/12/2023
# previously: 0 stars

inputFile = 'year_2022/day 7/example.txt'
inputFile = 'aoc-inputs/year_2022/day 7/input.txt'

dir = '/'
dir_map = {}
dir_size = 0

for line in open(inputFile).readlines():
    line = line.strip('\n')
    if line[:1] == '$':
        if 'cd' in line[2:4]:
            if dir_size:
                dir_map[dir] = dir_size
                dir_size = 0
            cd = line.split('cd')[-1].strip()
            if cd == '/':
                dir = cd
                continue
            if cd == '..':
                dir = '/'.join(d for d in dir.split('/')[:-2])
                dir += '/'
            else:
                dir += cd+'/'
        if 'ls' in line:
            continue
    else:
        if line[:3] == 'dir':
            continue
        dir_size += int(line.split()[0])
if dir_size:
    dir_map[dir] = dir_size
    dir_size = 0

size_map = {}

for cdir,size in dir_map.items():
    for dirs in cdir.split('/'):
        if dirs in size_map:
            size_map[dirs] += size
        else:
            size_map[dirs] = size

part1_total = 0

for dirs,size in size_map.items():
    # print(f'/{dirs}:{size}')
    if size <= 100000:
        part1_total += size

print(f'part 1 answer is: {part1_total}')
