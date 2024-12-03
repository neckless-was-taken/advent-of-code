# input = 'year_2024/day 3/example.txt'
input = 'aoc-inputs/year_2024/day 3/input.txt'

import re

computer_memory = ""
for line in open(input).readlines():
    computer_memory += str(line.strip('\n'))

instructions = re.findall(r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)', computer_memory)

answer_1 = 0

while instructions:
    current_instruction = list(map(int, instructions.pop().strip('mul(').strip(')').split(',')))
    answer_1 += current_instruction[0] * current_instruction[1]

print(f'answer to part 1: {answer_1}')

# part 2

answer_2 = 0

instructions = re.findall(r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)|do\(\)|don\'t\(\)', computer_memory)

do = 1
while instructions:
    current_instruction = instructions.pop(0)
    if current_instruction == "don't()":
        do = 0
        continue
    elif current_instruction == "do()":
        do = 1
    else:
        if do:
            current_instruction = list(map(int, current_instruction.strip('mul(').strip(')').split(',')))
            answer_2 += current_instruction[0] * current_instruction[1]

print(f'answer to part 2: {answer_2}')