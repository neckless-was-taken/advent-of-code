inputFile = 'day 3/example1.txt'
inputFile = 'day 3/input.txt'

input = open(inputFile, 'r')
schematic = []
for lines in input.readlines():
    lines = lines.strip('\n')
    line = []
    for char in lines:
        line.append(char)
    schematic.append(line)
input.close()

def isItaGear(y,x,schematic):
    ratios = []
    # line above
    if y > 0:
        if schematic[y-1][x].isdigit():
            ratios.append(schematic[-y][x])
        else:
            if x > 0:
                if schematic[y-1][x-1].isdigit():
                    ratios.append(schematic[y-1][x])
            if x < len(schematic[y-1])-1:
                if schematic[y-1][x+1].isdigit():
                    ratios.append(schematic[y-1][x])
    # current line
    if x > 0:
        if schematic[y][x-1].isdigit():
            ratios.append(schematic[y][x-1])
    if x < len(schematic[y])-1:
        if schematic[y][x+1].isdigit():
            ratios.append(schematic[y][x+1])

    # line below
    if y < len(schematic)-1:
        if schematic[y+1][x].isdigit():
            ratios.append(schematic[y+1][x])
        else:
            if x > 0:
                if schematic[y+1][x-1].isdigit():
                    ratios.append(schematic[y+1][x])
            if x < len(schematic[y+1])-1:
                if schematic[y+1][x+1].isdigit():
                    ratios.append(schematic[y+1][x])
    if len(ratios) == 2:
        return True
    else:
        return False
    
def gearRatioCalc(y,x,schematic):
    ratios = []
    currRatio = ''
    start = False

    print(y, x)
    pass

    # current line
    indexDict = {}
    for i, char in enumerate(schematic[y]):
        if char.isdigit():
            indexDict[i] = char
    if len(indexDict) != 0:
        if x > 0:
            start = False
            if schematic[y][x-1].isdigit():
                for i in range(x-1,-1,-1):
                    if not schematic[y][i].isdigit():
                        break
                    start = i
                if start != False or start == 0:
                    for i in range(start,len(schematic[y])-1):
                            if schematic[y][i].isdigit():
                                currRatio += str(schematic[y][i])
                            else:
                                break
                    if len(currRatio) != 0:
                        ratios.append(currRatio)
                        currRatio = ''
    if x < len(schematic[y])-1:
        start = False
        if schematic[y][x+1].isdigit():
            start = x+1
            if start != False or start == 0:
                for i in range(start,len(schematic[y])-1):
                    if schematic[y][i].isdigit():
                        currRatio += str(schematic[y][i])
                    else:
                        break
                if len(currRatio) != 0:
                    ratios.append(currRatio)
                    currRatio = ''

    # line above
    if y > 0:
        if x > 0:
            j = x-1
        else:
            j = x
        if schematic[y-1][j].isdigit() or schematic[y-1][x].isdigit() or schematic[y-1][x+1].isdigit():
            # print(schematic[y-1])
            indexDict = {}
            for i, char in enumerate(schematic[y-1]):
                if char.isdigit():
                    indexDict[i] = char
            if len(indexDict) != 0:
                if x < len(schematic[y-1])-1:
                    b = x+1
                else:
                    b = x
                start = False
                for i in range(b,-1,-1):
                    if schematic[y-1][i].isdigit():
                        start = i
                        pass
                    else:
                        if start:
                            break
                if start != False or start == 0:
                    for i in range(start,len(schematic[y-1])):
                        if schematic[y-1][i].isdigit():
                            currRatio += str(schematic[y-1][i])
                        else:
                            break
                    if len(currRatio) != 0:
                        ratios.append(currRatio)
                        currRatio = ''
                if len(ratios) != 2 and start == x+1 and x != 0:
                    start = False
                    b = x-1
                    for i in range(b,-1,-1):
                        if schematic[y-1][i].isdigit():
                            start = i
                            pass
                        else:
                            if start or start < x-1:
                                break
                    if start != False or start == 0:
                        for i in range(start,len(schematic[y-1])):
                            if schematic[y-1][i].isdigit():
                                currRatio += str(schematic[y-1][i])
                            else:
                                break
                        if len(currRatio) != 0:
                            ratios.append(currRatio)
                            currRatio = ''

    # line below
    if y < len(schematic)-1:
        if x > 0:
            j = x-1
        else:
            j = x
        if schematic[y+1][j].isdigit() or schematic[y+1][x].isdigit() or schematic[y+1][x+1].isdigit():
            # print(schematic[y+1])
            indexDict = {}
            for i, char in enumerate(schematic[y+1]):
                if char.isdigit():
                    indexDict[i] = char
            if len(indexDict) != 0:
                if x < len(schematic[y+1])-1:
                    b = x+1
                else:
                    b = x
                start = False
                for i in range(b,-1,-1):
                    if schematic[y+1][i].isdigit():
                        start = i
                        pass
                    else:
                        if start:
                            break
                if start != False or start == 0:
                    for i in range(start,len(schematic[y+1])):
                        if schematic[y+1][i].isdigit():
                            currRatio += str(schematic[y+1][i])
                        else:
                            break
                    if len(currRatio) != 0:
                        ratios.append(currRatio)
                        currRatio = ''
                if len(ratios) != 2 and start == x+1 and x != 0:
                    b = x-1
                    start = False
                    for i in range(b,-1,-1):
                        if schematic[y+1][i].isdigit():
                            start = i
                            pass
                        else:
                            if start:
                                break
                    if start != False or start == 0:
                        for i in range(start,len(schematic[y+1])):
                            if schematic[y+1][i].isdigit():
                                currRatio += str(schematic[y+1][i])
                            else:
                                break
                        if len(currRatio) != 0:
                            ratios.append(currRatio)
                            currRatio = ''
    if len(ratios) != 2:
        pass
    if ratios[0] == ratios[1]:
        pass
    print(ratios)
    return int(ratios[0])*int(ratios[1])

sum = 0

for y, line in enumerate(schematic):
    for x, char in enumerate(line):
        if char == '*':
           valid = isItaGear(y,x,schematic)
           if valid:
               gearRatio = gearRatioCalc(y,x,schematic)
               sum += gearRatio

print(sum)