# inputFile = 'day 3/example1.txt'
inputFile = 'day 3/input.txt'

input = open(inputFile, 'r')
schematic = []
for line in input.readlines():
    schematic.append(line.strip('\n'))
input.close()

def getPartNumber(currKey,indexDict):
    partNumber = str(indexDict.get(currKey))
    i = int(currKey)
    indexDict.pop(i)
    start = i
    while True:
        i += 1
        if indexDict.get(i) == None:
            end = i-1
            break
        else:
            partNumber += str(indexDict.get(i))
            indexDict.pop(i)
    return start,end,partNumber,indexDict

def symbolCheck(start, end, n, schematic):
    if end != len(schematic[n]):
        isValid = oneAfter(end,n,schematic)
        if isValid:
            return True
    if start != 0:
        isValid = oneBefore(start,n,schematic)
        if isValid:
            return True
    if n != 0:
        a = n-1
        isValid = oneAboveOneBelow(start,end,a,schematic)
        if isValid:
            return True
    if n != len(schematic)-1:
        b = n+1
        isValid = oneAboveOneBelow(start,end,b,schematic)
        if isValid:
            return True
    return False
    
def oneBefore(start,n,schematic):
    for i,char in enumerate(schematic[n]):
        if i == start-1:
            if char.isdigit() or char == '.':
                break
            else:
                return True
    return False

def oneAfter(end,n,schematic):
    for i,char in enumerate(schematic[n]):
        if i == end+1:
            if char.isdigit() or char == '.':
                break
            else:
                return True
    return False

def oneAboveOneBelow(start,end,n,schematic):
    # print(f'checking line: {schematic[n]}')
    if start != 0:
        start -= 1
    if end != len(schematic[n]):
        end += 1
    for i,char in enumerate(schematic[n]):
        if i < start or i > end:
            continue
        else:
            if not char.isdigit() and not char == '.':
                return True
    return False

sum = 0

for n,line in enumerate(schematic):
    # # test case
    # n = 2
    # line = '..35..633.'
    # # test case
    partNumber = ''
    indexDict = {}
    # print(f'{n}: {line}')
    for index, char in enumerate(line):
        if char.isdigit():
            indexDict[index] = char
    # print(indexDict)
    while True:
        try:
            currkey = min(indexDict.keys())
        except ValueError:
            break
        start, end, partNumber, indexDict = getPartNumber(currkey,indexDict)
        isValid = symbolCheck(start, end, n, schematic)
        if isValid:
            sum += int(partNumber)

print(sum)
# EOL