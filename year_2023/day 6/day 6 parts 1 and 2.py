# inputFile = 'year_2023/day 6/example1.txt'
inputFile = 'aoc-inputs/year_2023/day 6/input.txt'

# Distance = Velocity*Time + 1/2*(Acceleration*Time**2)
# Distance = Velocity*Time

def part1(time, distance):
    margin = []
    for e, t in enumerate(time):
        t = int(t)
        waysToWin = 0
        for i in range(t+1):
            d = i*(t-i)
            if d > int(distance[e]):
                waysToWin += 1
        margin.append(waysToWin)
    return margin

def part2(time, distance):
    waysToWin = 0
    for i in range(time+1):
        d = i*(time-i)
        if d > distance:
            waysToWin += 1
    return waysToWin


for line in open(inputFile, 'r').readlines():
    if 'Time:' in line:
        time = line.strip('\n').split('Time:')[1].split()
    elif 'Distance:' in line:
        distance = line.strip('\n').split('Distance:')[1].split()

# part 1
errorMargin = part1(time, distance)
x = False
for i in errorMargin:
    if not x:
        x = i
    else:
        x = x*i

print(f'Part 1: {x}')

# part 2
newTime = ''
for t in time:
    newTime += str(t)
newTime = int(newTime)
newDistance = ''
for d in distance:
    newDistance += str(d)
newDistance = int(newDistance)

errorMargin = part2(newTime, newDistance)
print(f'Part 2: {errorMargin}')