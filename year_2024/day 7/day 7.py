input = 'year_2024/day 7/example.txt'
input = 'aoc-inputs/year_2024/day 7/input.txt'

from tqdm import tqdm

def operator_finder3000(calib):
    result = calib[0]
    equation = list(calib[1:])

    if len(equation) == 1: return result
    if len(equation) == 2:
        if equation[0] + equation[1] == result: return result
        if equation[0] * equation[1] == result: return result
    else:
        temp = 0
        for e in equation: # all +
            temp += e
        if temp == result: return result

        temp = 1
        for e in equation: # all *
            temp *= e
        if temp == result: return result

        for i in range(2**(len(equation)-1)):
            binary = format(i, f'0{len(equation)-1}b') 

            temp = equation[0]
            for e, digit in enumerate(binary):
                if digit == '1':
                    temp *= equation[e+1]
                elif digit == '0':
                    temp += equation[e+1]
            if temp == result: return result

    return 0

def third_operator(calib):
    result = calib[0]
    equation = list(calib[1:])

    for i in range(3**(len(equation)-1)):
        n = i
        base_3 = ''
        for _ in range(len(equation)-1):
            base_3 = str(n % 3) + base_3
            n //= 3

        temp = equation[0]
        for e, digit in enumerate(base_3):
            if digit == '1':
                temp *= equation[e+1]
            elif digit == '0':
                temp += equation[e+1]
            elif digit == '2':
                temp = int(str(temp) + str(equation[e+1]))
        if temp == result: return result
    return 0

answer_1 = 0
answer_2 = 0

print()
for line in tqdm(open(input).readlines()):
    line = str(line.strip('\n'))
    calibration = (list(map(int, line.replace(':', '').split())))
    binary = operator_finder3000(calibration)
    answer_1 += binary
    if binary > 0:
        answer_2 += binary
    else:
        answer_2 += third_operator(calibration)
    

print(answer_1)
print(answer_2)
