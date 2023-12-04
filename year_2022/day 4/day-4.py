answer1 = 0
answer2 = 0

# inputFile = 'year_2022/day 4/example.txt'
inputFile = 'aoc-inputs/year_2022/day 4/input.txt'

input = open(inputFile,'r')

while True:
    elf1_tasks= ''
    elf2_tasks= ''
    answer2_trigger = False
    pair = input.readline()
    if not pair:
        break
    elf1, elf2 = pair.split(',')
    elf1_task_start_input, elf1_task_end_input = elf1.split('-')
    elf2_task_start_input, elf2_task_end_input = elf2.split('-')
    elf1_task_start=int(elf1_task_start_input)
    elf2_task_start=int(elf2_task_start_input)
    elf1_task_end=int(elf1_task_end_input)
    elf2_task_end=int(elf2_task_end_input)
    

    while elf1_task_start != elf1_task_end + 1:
        elf1_task = str(elf1_task_start)
        elf1_tasks += '-'+elf1_task+'-'
        elf1_task_start += 1

    while elf2_task_start != elf2_task_end + 1:
        elf2_task = str(elf2_task_start)
        elf2_current_task = '-'+elf2_task+'-'
        elf2_tasks += '-'+elf2_task+'-'
        elf2_task_start += 1
        if elf2_current_task in elf1_tasks:
            answer2_trigger = True
    print('elf1_tasks = '+elf1_tasks+' elf2_tasks = '+elf2_tasks)
    if elf1_tasks in elf2_tasks:
        answer1 += 1
        print('first case true')
    else:
        if elf2_tasks in elf1_tasks:
            answer1 += 1
            print('second case true')
        else:
            print('both cases false')
            pass
    if answer2_trigger is True:
        answer2 += 1
    else:
        pass
    ## SECOND PART
    

answer1 = str(answer1)
print('answer to the first section = '+answer1)
answer2 = str(answer2)
print('answer to the second section = '+answer2)