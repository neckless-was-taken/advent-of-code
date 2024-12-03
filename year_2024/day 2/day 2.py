# input = 'year_2024/day 2/example.txt'
input = 'aoc-inputs/year_2024/day 2/input.txt'


answer_1 = 0
answer_2 = 0

def safety_checker(curr_line):
    direction = 0
    for x in range(len(curr_line)):
        if x == len(curr_line)-1: # reached the end
            return 1
        a, b = curr_line[x], curr_line[x+1]

        if a == b: # not decreasing or increasing
            return 0
        
        if abs(a - b) > 3:
            return 0

        if b - a > 0: # is increasing
            y = b - a
            if direction == 0:
                direction = 1
            if direction != 1:
                return 0
            
        elif a - b > 0: # is decreasing
            if direction == 0:
                direction = -1
            if direction != -1:
                return 0       
    return 0

for line in open(input).readlines():
    is_safe = 0
    line = list(map(int,str(line.strip('\n')).split()))

    is_safe = safety_checker(line)
    if is_safe:
        answer_1 += 1

    else:
        for x in range(len(line)):
            maybe_safe = safety_checker(line[:x] + line[x+1:])
            if maybe_safe:
                answer_2 += 1
                break

    pass
print(answer_1)

print(answer_1 + answer_2)