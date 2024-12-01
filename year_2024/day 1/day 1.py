# input = 'year_2024/day 1/example.txt'
input = 'aoc-inputs/year_2024/day 1/input.txt'

answer_1 = 0
left_list = dict()
right_list = dict()
for e, line in enumerate(open(input).readlines()):
    line = str(line.strip('\n'))
    left_list[e] = line.split()[0]
    right_list[e] = line.split()[1]

while left_list:
    answer_1 += abs(int(left_list.pop(min(left_list, key = left_list.get))) - int(right_list.pop(min(right_list, key = right_list.get))))

print(f'answer to part 1: {answer_1}')

answer_2 = 0
left_list = []
right_list = []

for line in open(input).readlines():
    line = str(line.strip('\n'))
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[-1]))

while left_list:
    a = left_list.pop(0)
    answer_2 += a * right_list.count(a)

print(f'answer to part 2: {answer_2}')