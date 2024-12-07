input = 'year_2024/day 6/example.txt'
# input = 'aoc-inputs/year_2024/day 6/input.txt'

lab_map = []

def guard_path(start):
    new_map = lab_map
    location_r = start[0]
    location_c = start[1]
    direction = '^'

    # answer_2 = 0
    # last_turns = ['a']
    # new_desks = [] # we are adding new desks to the North Pole prototype suit manufacturing lab!
    # step = 0


    while True:


        # This is a failed attempt at solving Part 2
        # This algorithm looks to place the guard in a rectangle shaped loop rather than any loop possible
        # Thankfully AoC creators were kind enough to provide an example with a non-rectangle loop :) thanks
        # But I only noticed when running the example resulted in 1 possibilty missed
        # 
        # if len(last_turns) == 3:
        #     if last_turns[0] == 'a':
        #         pass
        #     else:
        #         first_turn = last_turns[0]
        #         if direction == '^':
        #             if location_r == first_turn[0]:
        #                 if location_r - 1 > 0:
        #                     if [location_r - 1, location_c] not in new_desks:
        #                         new_desks.append([location_r - 1, location_c])
                
        #         if direction == 'v':
        #             if location_r == first_turn[0]:
        #                 if location_r + 1 < len(new_map):
        #                     if [location_r + 1, location_c] not in new_desks:
        #                         new_desks.append([location_r + 1, location_c])
                
        #         if direction == '<':
        #             if location_c == first_turn[1]:
        #                 if location_c - 1 > 0:
        #                     if [location_r, location_c - 1] not in new_desks:
        #                         new_desks.append([location_r, location_c - 1])
        #         if direction == '>':
        #             if location_c == first_turn[1]:
        #                 if location_c + 1 < len(new_map[location_r]):
        #                     if [location_r, location_c + 1] not in new_desks:
        #                         new_desks.append([location_r, location_c + 1])

        if direction == '^':
            try:
                if new_map[location_r-1][location_c] == '#':
                    new_location_r = location_r
                    new_location_c = location_c + 1
                    direction = '>'

                    new_map[location_r][location_c] = 'x'
                    # if len(last_turns) == 3:
                    #     last_turns = last_turns[1:]
                    #     last_turns.append([location_r, location_c])
                    # else:
                    #     last_turns.append([location_r, location_c])
                else:
                    new_location_r = location_r - 1
                    new_location_c = location_c
                    if new_map[location_r][location_c] in '<>x':
                        new_map[location_r][location_c] = 'x'
                    else:
                        new_map[location_r][location_c] = '^'
                # new_map[new_location_r][new_location_c] = 'X'
            except IndexError:
                break
        
        elif direction == '>':
            try:
                if new_map[location_r][location_c+1] == '#':
                    new_location_r = location_r + 1
                    new_location_c = location_c
                    direction = 'v'

                    new_map[location_r][location_c] = 'x'
                    # if len(last_turns) == 3:
                    #     last_turns = last_turns[1:]
                    #     last_turns.append([location_r, location_c])
                    # else:
                    #     last_turns.append([location_r, location_c])
                else:
                    new_location_r = location_r
                    new_location_c = location_c + 1
                    if new_map[location_r][location_c] in '^vx':
                        new_map[location_r][location_c] = 'x'
                    else:
                        new_map[location_r][location_c] = '>'
                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
        
        elif direction == 'v':
            try:
                if new_map[location_r+1][location_c] == '#':
                    new_location_r = location_r
                    new_location_c = location_c - 1
                    direction = '<'

                    new_map[location_r][location_c] = 'x'
                    # if len(last_turns) == 3:
                    #     last_turns = last_turns[1:]
                    #     last_turns.append([location_r, location_c])
                    # else:
                    #     last_turns.append([location_r, location_c])
                else:
                    new_location_r = location_r + 1
                    new_location_c = location_c
                    if new_map[location_r][location_c] in '<>x':
                        new_map[location_r][location_c] = 'x'
                    else:
                        new_map[location_r][location_c] = 'v'
                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
            
        elif direction == '<':
            try:
                if new_map[location_r][location_c-1] == '#':
                    new_location_r = location_r - 1
                    new_location_c = location_c
                    direction = '^'

                    new_map[location_r][location_c] = 'x'
                    # if len(last_turns) == 3:
                    #     last_turns = last_turns[1:]
                    #     last_turns.append([location_r, location_c])
                    # else:
                    #     last_turns.append([location_r, location_c])
                else:
                    new_location_r = location_r
                    new_location_c = location_c - 1
                    if new_map[location_r][location_c] in '^vx':
                        new_map[location_r][location_c] = 'x'
                    else:
                        new_map[location_r][location_c] = '<'
                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
        location_r = new_location_r
        location_c = new_location_c
    new_map[location_r][location_c] = direction
    return new_map

def loop_finder3000(new_map, start):
    step = 0
    location_r = start[0]
    location_c = start[1]
    direction = '^'

    visited = [[r, c, direction]]

    while True:
        step += 1
        if direction == '^':
            try:
                if new_map[location_r-1][location_c] == '#':
                    new_location_r = location_r
                    new_location_c = location_c + 1
                    direction = '>'
                else:
                    new_location_r = location_r - 1
                    new_location_c = location_c

                # new_map[new_location_r][new_location_c] = 'X'
            except IndexError:
                break
        
        elif direction == '>':
            try:
                if new_map[location_r][location_c+1] == '#':
                    new_location_r = location_r + 1
                    new_location_c = location_c
                    direction = 'v'

                else:
                    new_location_r = location_r
                    new_location_c = location_c + 1

                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
        
        elif direction == 'v':
            try:
                if new_map[location_r+1][location_c] == '#':
                    new_location_r = location_r
                    new_location_c = location_c - 1
                    direction = '<'

                else:
                    new_location_r = location_r + 1
                    new_location_c = location_c

                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
            
        elif direction == '<':
            try:
                if new_map[location_r][location_c-1] == '#':
                    new_location_r = location_r - 1
                    new_location_c = location_c
                    direction = '^'
                else:
                    new_location_r = location_r
                    new_location_c = location_c - 1
  
                # new_map[new_location_r][new_location_c] = 'X'

            except IndexError:
                break
        location_r = new_location_r
        location_c = new_location_c

        if [location_r, location_c, direction] in visited:
            return 1
        else:
            visited.append([location_r, location_c, direction])
    return 0



for r, line in enumerate(open(input).readlines()):
    line = str(line.strip('\n'))
    row = []
    for c, ch in enumerate(line):
        if ch == "^":
            start_location = [r, c]
        row.append(ch)
    lab_map.append(row)

updated_map = guard_path(start_location)

answer_1 = 0

for r, row in enumerate(updated_map):
    for c, col in enumerate(row):
        print(col, end="")
        if col in "<>v^x": # modified for part 2, initially this was {if col == 'X':} and the guard_path function placed Xs on each square she visits
            # I didn't end up using this functionality in the end but left it in
            answer_1 += 1
    print()
print()
print(f'answer to part 1: {answer_1}')
print()
# answer_2 = len(new_desks) # this didn't work as per the comments in guard_path function
# 

# commence operation hammer (brute-force)

answer_2 = 0

an_original_fucking_map_please = []

for i in open(input).readlines():
    i = str(i.strip('\n'))
    ji = []
    for j in i:
        ji.append(j)
    an_original_fucking_map_please.append(ji)

paradox_map = an_original_fucking_map_please.copy()

for i in paradox_map:
    print(i)
print()

for r, row in enumerate(paradox_map):
    for c, col in enumerate(row):
        if col == '.':
            paradox_map[r][c] = '#'
            for cunt in paradox_map:
                print(cunt)
            answer_2 += loop_finder3000(paradox_map, start_location)
            print()
            paradox_map[r][c] = '.'
            


print(f'answer to part 2: {answer_2}')