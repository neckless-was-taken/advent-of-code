# input = 'year_2022/day 11/example.txt'
# input = 'aoc-inputs/year_2022/day 11/input.txt'

# lines = [str(line.strip('\n')) for line in open(input,'r').readlines()]

# monkey = []
# c_monkey = []

# for i in lines:
#     #print(i)
#     if i in 'Starting items:':
#         c_monkey.append(i)
#     if i in 'Monkey':
#         monkey.append(c_monkey)
#         c_monkey = []

# print(monkey)

monkey = [[89,73,66,57,64,80],[83,78,81,55,81,59,69],[76,91,58,85],[71,72,74,76,68],[98,85,84],[78],[86, 70, 60, 88, 88, 78, 74, 83],[81, 58]]

inspection_count = [0,0,0,0,0,0,0,0]

def monkey0_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[0][0]
            c_item *= 3
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%13 == 0:
                monkey[6].append(c_item)
            else:
                monkey[2].append(c_item)
            monkey[0].pop(0)
            inspection_count[0] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey1_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[1][0]
            c_item += 1
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%3 == 0:
                monkey[7].append(c_item)
            else:
                monkey[4].append(c_item)
            monkey[1].pop(0)
            inspection_count[1] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey2_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[2][0]
            c_item *= 13
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%7 == 0:
                monkey[1].append(c_item)
            else:
                monkey[4].append(c_item)
            monkey[2].pop(0)
            inspection_count[2] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey3_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[3][0]
            c_item *= c_item
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%2 == 0:
                monkey[6].append(c_item)
            else:
                monkey[0].append(c_item)
            monkey[3].pop(0)
            inspection_count[3] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey4_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[4][0]
            c_item += 7
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%19 == 0:
                monkey[5].append(c_item)
            else:
                monkey[7].append(c_item)
            monkey[4].pop(0)
            inspection_count[4] += 1
        except:
            break
        break   
    return monkey, inspection_count

def monkey5_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[5][0]
            c_item += 8
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%5 == 0:
                monkey[3].append(c_item)
            else:
                monkey[0].append(c_item)
            monkey[5].pop(0)
            inspection_count[5] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey6_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[6][0]
            c_item += 4
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%11 == 0:
                monkey[1].append(c_item)
            else:
                monkey[2].append(c_item)
            monkey[6].pop(0)
            inspection_count[6] += 1
        except:
            break
        break
    return monkey, inspection_count

def monkey7_instructions(monkey, inspection_count):
    while True:
        try:
            c_item = monkey[7][0]
            c_item += 5
            #c_item = int(c_item/3) # answer 1
            c_item %= mod
            if c_item%17 == 0:
                monkey[3].append(c_item)
            else:
                monkey[5].append(c_item)
            monkey[7].pop(0)
            inspection_count[7] += 1
        except:
            c_item = 0
            break
        break
    return monkey, inspection_count

mod = 13*3*7*2*19*5*11*17
monkey4_insp_c = 0
monkey2_insp_c = 0


for i in range(0,10000):
    monkey, inspection_count = monkey0_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey1_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey2_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey3_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey4_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey5_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey6_instructions(monkey, inspection_count)
    monkey, inspection_count = monkey7_instructions(monkey, inspection_count)
    #if i in rounds:
    #print("current round :",i)

#print("finished the shit 8)")
print(inspection_count)

a = sorted(inspection_count, reverse=True)
print(a[0]*a[1])