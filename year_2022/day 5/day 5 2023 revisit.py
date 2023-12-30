# revisit date: 30/12/2023
# previously: 0 stars

# inputFile = 'year_2022/day 5/example.txt'
inputFile = 'aoc-inputs/year_2022/day 5/input.txt'

def moveBoxes(instructions, stacks):
    count, source, dest = instructions
    for _ in range(int(count)):
        stacks[int(dest)-1].append(stacks[int(source)-1].pop(-1))
    return stacks

def moveBoxes9001(instructions, stacks):
    count, source, dest = instructions
    boxes = ''
    for _ in range(int(count)):
        boxes += stacks[int(source)-1].pop(-1)
    for box in boxes[::-1]:
        stacks[int(dest)-1].append(box)
    return stacks

instruction_list = []
stacks = [[],[],[],[],[],[],[],[],[]]
start_stacks = [[],[],[],[],[],[],[],[],[]]

for line in open(inputFile).readlines():
    line = line.strip('\n')

    if "move" in line:
        instructions = line.split()[1::2]
        instruction_list.append(instructions)
        stacks = moveBoxes(instructions,stacks)

    # generate the list of the stacks
    elif '[' in line:
        for i, ch in enumerate(line):
            if ch in ' []':
                continue
            stacks[i//4].append(ch)

    elif '1   2   3' in line:
        # reverse the stacks to make them easier to work with append(pop(-1))
        for i, stack in enumerate(stacks):
            if not stack:
                continue
            stacks[i] = [ch for ch in stack[::-1]]
            start_stacks[i] = [ch for ch in stack[::-1]]


print('part 1 answer: ',end='')
for stack in stacks:
    if stack:
        print(''.join(stack[-1]), end='')
print()


stacks = start_stacks
for n in range(len(instruction_list)):
    stacks = moveBoxes9001(instruction_list[n],stacks)


print('part 2 answer: ',end='')
for stack in stacks:
    if stack:
        print(''.join(stack[-1]), end='')
print()
pass