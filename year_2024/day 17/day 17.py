input = 'year_2024/day 17/example.txt'
input = 'aoc-inputs/year_2024/day 17/input.txt'

from functools import cache
from tqdm import tqdm

@cache
def adv(n,d):
    '''
    n = register A

    d = combo operand
    
    returns register A'''

    return int(n/(2**d))

@cache
def bxl(a,b):
    '''
    a = register B

    b = literal operand

    returns register B'''
    return int(a^b)

@cache
def bst(a):
    '''
    a = combo operand

    returns register B'''
    return a % 8

def jnz():
    '''
    returns 0 or 1, if 1 pointer jumps to literal operand'''
    return 0 if register_A == 0 else 1

@cache
def bxc(a,b):
    '''
    a = register B
    
    b = register C
    
    returns register B'''
    return a ^ b

@cache
def out(a):
    '''
    a = combo operand
    
    returns output'''
    return a % 8

@cache
def bdv(a,b):
    '''
    a = register A
    
    b = combo operand
    
    returns register B'''
    return adv(a,b)

@cache
def cdv(a,b):
    '''
    a = register A
    
    b = combo operand
    
    returns register C'''
    return adv(a,b)

program = []
register_A = 0
register_B = 0
register_C = 0

c = 0
x = []

for line in open(input).readlines():
    line = str(line.strip('\n'))
    if 'Register A' in line:
        register_A = int(line.split()[-1])
    elif 'Register B' in line:
        register_B = int(line.split()[-1])
    elif 'Register C' in line:
        register_C = int(line.split()[-1])
    elif 'Program' in line:
        line = line.split()[-1]
        for i in line.split(','):
            x.append(int(i))
            c += 1
            if c == 2:
                program.append(x)
                c = 0
                x = []

# print(f'Register A: {register_A}')
# print(f'Register B: {register_B}')
# print(f'Register C: {register_C}')
# print(f'Program: {program}')

# for part 2
input_program = str('')
for i in program:
    for j in i:
        input_program += f'{str(j)},'
input_program = input_program[0:-1]
# 

part_1 = 0
initial_register_A = int(register_A)
initial_register_B = int(register_B)
initial_register_C = int(register_C)

for x in tqdm(range(999999999999999)):
    register_A = x
    register_B = initial_register_B
    register_C = initial_register_C
    if register_A == initial_register_A:
        part_1 = 1
    output = str('')
    pointer = 0
    halt = 0
    while not halt:
        i = pointer
        for opcode, operand in program[pointer:]:
            i += 1
            if 0 <= operand <= 3:
                combo = operand
            elif operand == 4:
                combo = register_A
            elif operand == 5:
                combo = register_B
            elif operand == 6:
                combo = register_C
            elif operand == 7:
                print('Invalid operand: 7')
            else:
                print(f'Invalid operand: {operand}')

            
            if opcode == 3:
                if jnz():
                    pointer = int(operand / 2)
                    break
            elif opcode == 0:
                register_A = adv(register_A, combo)
            elif opcode == 1:
                register_B = bxl(register_B, operand)
            elif opcode == 2:
                register_B = bst(combo)
            elif opcode == 4:
                register_B = bxc(register_B, register_C)
            elif opcode == 5:
                output += f'{out(combo)},'
            elif opcode == 6:
                register_B = bdv(register_A, combo)
            elif opcode == 7:
                register_C = cdv(register_A, combo)

            if i == len(program):
                halt = 1
    output = output[0:-1]
    if part_1:
        print(f'answer to part 1: {output}')
        part_1 = 0
    
    if output == input_program:
        print(f'answer to part 2: {x}')
        break
    

# print(f'Register A: {register_A}')
# print(f'Register B: {register_B}')
# print(f'Register C: {register_C}')
# print(f'Program: {program}')

