# input = 'year_2022/day 10/example.txt'
input = 'aoc-inputs/year_2022/day 10/input.txt'

x = 1
signal_strength = [int(0)]

instructions = [str(line.strip('\n')) for line in open(input,'r').readlines()]

instruction_list = ["start"]

for i in instructions:
    if "noop" in i:
        signal_strength.append(x)
        instruction_list.append(i)
    if "addx" in i:
        signal_strength.append(x)
        instruction_list.append(i)
        signal_strength.append(x)
        instruction_list.append(i)
        x += int(i.split()[-1])

sum = 0

interesting_cycles = [20, 60, 100, 140, 180, 220]

for cycle in range(0,len(signal_strength)):
    #print(cycle,signal_strength[cycle],instruction_list[cycle])
    if cycle in interesting_cycles:
       #print(cycle,signal_strength[cycle],cycle*signal_strength[cycle])
       sum += cycle*signal_strength[cycle]

print("answer 1 is :",sum)
print()
crt_lines = [40, 80, 120, 160, 200]
current_pixel = 0

for cycle in range(1,len(signal_strength)):
    sprite_position = [signal_strength[cycle]-1,signal_strength[cycle],signal_strength[cycle]+1]
    if current_pixel in sprite_position:
        print('#', end='')
    else:
        print('.', end='')
    # print('-', end='')
    current_pixel += 1
    if cycle in crt_lines:
        current_pixel = 0
        print()