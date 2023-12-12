# input = 'year_2022/day 1/example.txt'
input = 'aoc-inputs/year_2022/day 1/input.txt'

elf = []
c_elf = []
t_elf = []
cal = 0

calories = [line.strip('\n') for line in open(input).readlines()]
# print(calories)
for c in calories:
    if c != '':
        c_elf.append(int(c))
    else:
        elf.append(c_elf)
        c_elf = []

# print("elf:",elf)

for i in range(0,len(elf)):
    for j in range(0,len(elf[i])):
        cal = cal + elf[i][j]
    t_elf.append(cal)
    cal = 0
print(max(t_elf))

a = sorted(t_elf, reverse=True)
sum = a[0]+a[1]+a[2]
print(sum)
