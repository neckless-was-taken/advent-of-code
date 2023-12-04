# input = 'year_2022/day 2/example.txt'
input = 'aoc-inputs/year_2022/day 2/input.txt'

A = ['A','B','C']
X = ['X','Y','Z']
RPS = ['R','P','S']

instructions = [list(line.strip('\n').replace("A","R").replace("B","P").replace("C","S").replace("X","R").replace("Y","P").replace("Z","S").split()) for line in open(input,'r').readlines()]
# print(instructions)
points = 0

for i in range(0,len(instructions)):
    if instructions[i][1] == "R":
        points += 1
        if instructions[i][0] == "S":
            points += 6
        if instructions[i][0] == "P":
            points += 0
        if instructions[i][0] == "R":
            points += 3
    if instructions[i][1] == "P":
        points += 2
        if instructions[i][0] == "R":
            points += 6
        if instructions[i][0] == "S":
            points += 0
        if instructions[i][0] == "P":
            points += 3
    if instructions[i][1] == "S":
        points += 3
        if instructions[i][0] == "P":
            points += 6
        if instructions[i][0] == "R":
            points += 0
        if instructions[i][0] == "S":
            points += 3


print("points for strategy 1 :",points)

points = 0

for i in range(0,len(instructions)):
    instructions[i][1] = instructions[i][1].replace("R","X").replace("P","Y").replace("S","Z")

    if instructions[i][0] == "R":
        if instructions[i][1] == "X":
            points += 3
            points += 0
        if instructions[i][1] == "Y":
            points += 1
            points += 3
        if instructions[i][1] == "Z":
            points += 2
            points += 6
    if instructions[i][0] == "P":
        if instructions[i][1] == "X":
            points += 1
            points += 0
        if instructions[i][1] == "Y":
            points += 2
            points += 3
        if instructions[i][1] == "Z":
            points += 3
            points += 6
    if instructions[i][0] == "S":
        if instructions[i][1] == "X":
            points += 2
            points += 0
        if instructions[i][1] == "Y":
            points += 3
            points += 3
        if instructions[i][1] == "Z":
            points += 1
            points += 6

print("points for strategy 2 :",points)