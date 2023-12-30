# inputFile = 'year_2023/day 15/example.txt'
inputFile = 'aoc-inputs/year_2023/day 15/input.txt'

def hash_algo(s):
    h = 0
    for ch in s:
        h += ord(ch)
        h *= 17
        h %= 256
    return h

part1_total = 0

for step in open(inputFile, 'r').read().split(','):
    hash_value = hash_algo(step)
    part1_total += hash_value

print(f'part 1 answer: {part1_total}')

hash_map = {}

part2_total = 0

boxes = [[] for n in range(256)]
focal_lengths = {}

for step in open(inputFile, 'r').read().strip('\n').split(','):
    if '-' in step:
        label = step[:-1]
        if label not in hash_map:
            index = hash_algo(label)
            hash_map[label] = index
        else:
            index = hash_map[label]
        if label in boxes[index]:
            boxes[index].remove(label)
    if '=' in step:
        label, f_length = step.split('=')
        f_length = int(f_length)
        if label not in hash_map:
            index = hash_algo(label)
            hash_map[label] = index
        else:
            index = hash_map[label]
        if label not in boxes[index]:
            boxes[index].append(label)
        focal_lengths[label] = f_length

# print(boxes)
# print(focal_lengths)

for n, lenses in enumerate(boxes):
    if lenses:
        for i, lens in enumerate(lenses):
            part2_total += (n+1) * (i+1) * focal_lengths[lens]

print(f'part 2 answer: {part2_total}')