def function_instruction_list(instruction_line):   
    current_instructions = instruction_line.split(' ')
    box_move_count = int(current_instructions[1])
    starting_stack = int(current_instructions[3])-1
    finish_stack = int(current_instructions[5])-1
    return box_move_count, starting_stack, finish_stack

def function_moving(box_move_count, starting_stack, finish_stack, stack):
    for _ in range(0,box_move_count):
        #print(starting_stack)
        last_item = ''
        last_item = stack[starting_stack][-1]
        stack[finish_stack].append(last_item)
        stack[starting_stack].remove(last_item)
    return stack

answer1 = 0
answer2 = 0


# input_file = 'year_2022/day 5/example.txt'
input_file = 'aoc-inputs/year_2022/day 5/input.txt'

input = open(input_file, 'r') # real input
total_stack_height = 8
total_stack_amount = 9
stack = [[],[],[],[],[],[],[],[],[]]

new_line=[]
current_box = str()
line_count = 0
i = 0
line=[]
input_trigger = False
skip_lines = 0
instruction_lines = []

while True:
    current_line = input.readline()
    line_count += 1
    if not current_line:
        break
    if "1   2" in current_line:
        input_trigger = True
    if input_trigger == False:
        for element in current_line:
            if i < 3:
                current_box = current_box + element
                i += 1
            else:
                new_line.append(current_box)
                current_box = ''
                i = 0
        line.append(new_line)
        new_line=[]
    if input_trigger == True:
        if skip_lines != 2:
            skip_lines += 1
        else:
            current_line=current_line.replace('\n','')
            instruction_lines.append(current_line)
#print(line[0][0])

current_box_y = 0
current_box_x = 0
stack_index = 0


## todo instead of breaking while loop, read and categorize entire input file by using boolean triggers
while current_box_y < total_stack_height:
    while current_box_x < total_stack_amount:
        if '   ' not in line[current_box_y][current_box_x]:
            line[current_box_y][current_box_x]=line[current_box_y][current_box_x].replace('[', '').replace(']','')
            stack[stack_index].append(line[current_box_y][current_box_x])
        current_box_x += 1
        stack_index += 1
    current_box_x = 0
    stack_index = 0
    current_box_y += 1

sorted_stack_index = 0
sorted_stack=[]

#print(stack)

while stack_index < total_stack_amount:
    stack[stack_index].reverse()
    #last_item = stack[stack_index][-1]
    #stack[stack_index].remove(last_item)
    #print(stack[stack_index])
    stack_index += 1
#print(stack)

#for abc in range(0,9):
#    print(stack[abc])
#
#print()

#print(instruction_line)
with open('output.txt','w') as f:
    for l,abc in enumerate(range(0,9)):
        f.write(str(l))
        f.write('\n')
        for xyz in stack[abc]:
            f.write(xyz)
    for instruction_line in instruction_lines:
        box_move_count, starting_stack, finish_stack = function_instruction_list(instruction_line)
        #print(box_move_count, starting_stack, finish_stack)
        stack = function_moving(box_move_count, starting_stack, finish_stack, stack)
        f.write('\n')
        for abc in range(0,9):
            for xyz in stack[abc]:
                f.write(xyz)
            f.write('\n')
## todo take sorted stacks and turn into lists of strings
## perform move actions
#print(stack)
#for abc in range(0,9):
#    print(stack[abc])
#answer = ''
#
#for j in range(0,9):
#    answer += stack[j][-1]
#print(answer)