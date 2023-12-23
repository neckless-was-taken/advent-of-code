# inputFile = 'year_2023/day 8/example1.txt'
# inputFile = 'year_2023/day 8/example2.txt'
inputFile = 'aoc-inputs/year_2023/day 8/input.txt'

def part1(start,end,directions,input):
    i = 0
    stepCount = 0
    while True:
        if start != end:
            if i >= len(directions):
                i = 0
            if directions[i] == 'L':
                start = input.get(start)[0]
            elif directions[i] == 'R':
                start = input.get(start)[1]
            i += 1
            stepCount += 1
        else:
            break
    return stepCount

def part2(startList,directions,input):
    i = 0
    stepCount = 0
    while True:
        newList = []
        checkIfAtEnd = False
        for k in startList:
            clist = []
            for c in k:
                clist.append(c)
            if clist[2] != 'Z':
                checkIfAtEnd = False
                break
            checkIfAtEnd = True
        if checkIfAtEnd:
            break

        if i >= len(directions):
            i = 0
        if directions[i] == 'L':
            dir = 0
        elif directions[i] == 'R':
            dir = 1
        for node in startList:
            newList.append(input.get(node)[dir])
        startList = newList
        i += 1
        stepCount += 1
    return stepCount

start = 'AAA'
end = 'ZZZ'
startList = []

directions = []
setDirections = False
input = {}
for line in open(inputFile, 'r').readlines():
    line = line.strip('\n')
    if not setDirections:
        for c in line:
            directions.append(c)
        setDirections = True
    elif line != '':
        key, lr = line.split(' = ')
        left, right = lr.strip('(').strip(')').split(', ')
        input[key]= (left,right)
        chars = []
        for c in key:
            chars.append(c)
        if chars[2] == 'A':
            startList.append(key)
        
# print(directions)
# for k,v in input.items():
#     print(f'{k}:{v}')

p1 = part1(start,end,directions,input)
print(f'part 1 = {p1}')
# p2 = part2(startList,directions,input)
# print(f'part 2 = {p2}')