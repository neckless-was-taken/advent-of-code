# input = 'day 1/example2.txt'
input = 'day 1/input.txt'

digits = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# indexDict = {}

calibration = 0
for line in open(input).readlines():
    line = str(line.strip('\n'))
    # line = 'nineonenine'
    # line = 'sevenine'
    indexDict = {}
    for char in line:
        try:
            indexDict.update({line.index(str(char)):int(char)})
            break
        except ValueError:
            continue
    for char in reversed(line):
        try:
            indexDict.update({line.rindex(str(char)):int(char)})
            break
        except ValueError:
            continue

    for key,value in digits.items():
        if value in line:
            indexDict.update({line.index(str(value)):key})

        if value[::-1] in line[::-1]:
            indexDict.update({line.rindex(str(value)):key})

    firstNum = indexDict[min(indexDict)]
    lastNum = indexDict[max(indexDict)]
    ab = firstNum*10+lastNum
    calibration += firstNum*10+lastNum
    pass
print(calibration)