# input = 'day 1/example1.txt'
input = 'day 1/input.txt'
calibration = 0
for line in open(input).readlines():
    line = str(line.strip('\n'))
    for char in line:
        try:
            firstNum = int(char)
            break
        except ValueError:
            continue
    for char in reversed(line):
        try:
            lastNum = int(char)
            break
        except ValueError:
            continue
    calibration += firstNum*10+lastNum

print(calibration)