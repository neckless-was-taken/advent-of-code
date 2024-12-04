input = 'year_2024/day 4/example.txt'
input = 'aoc-inputs/year_2024/day 4/input.txt'


# ALL POSSIBLE XMAS SEARCH MAPS
# max_matrix = [
#     ['0 0', '0 1', '0 2', '0 3', '0 4', '0 5', '0 6'],
#     ['1 0', '1 1', '1 2', '1 3', '1 4', '1 5', '1 6'],
#     ['2 0', '2 1', '2 2', '2 3', '2 4', '2 5', '2 6'],
#     ['3 0', '3 1', '3 2', '3X3', '3 4', '3 5', '3 6'],
#     ['4 0', '4 1', '4 2', '4 3', '4 4', '4 5', '4 6'],
#     ['5 0', '5 1', '5 2', '5 3', '5 4', '5 5', '5 6'],
#     ['6 0', '6 1', '6 2', '6 3', '6 4', '6 5', '6 6'] ]

# min_matrix = [
#     ['0X0', '0 1', '0 2', '0X3'],
#     ['1 0', '1 1', '1 2', '1 3'],
#     ['2 0', '2 1', '2 2', '2 3'],
#     ['3X0', '3 1', '3 2', '3X3'] ]

# long_matrix = [
#     ['0 0', '0 1', '0 2', '0X3', '0 4', '0 5', '0 6'],
#     ['1 0', '1 1', '1 2', '1 3', '1 4', '1 5', '1 6'],
#     ['2 0', '2 1', '2 2', '2 3', '2 4', '2 5', '2 6'],
#     ['3 0', '3 1', '3 2', '3X3', '3 4', '3 5', '3 6'] ]

# tall_matrix = [
#     ['0 0', '0 1', '0 2', '0 3'],
#     ['1 0', '1 1', '1 2', '1 3'],
#     ['2 0', '2 1', '2 2', '2 3'],
#     ['3X0', '3 1', '3 2', '3X3'],
#     ['4 0', '4 1', '4 2', '4 3'], 
#     ['5 0', '5 1', '5 2', '5 3'], 
#     ['6 0', '6 1', '6 2', '6 3'] ]

from collections import deque

def compass(row, col, centre):

    # find the direction where XMAS must be written for 'X' and 'M' to be start of legal XMAS

    direction = str()
    if row < centre[0]:
        direction += "N"
    elif row > centre[0]:
        direction += "S"
    if col < centre[1]:
        direction += "W"
    elif col > centre[1]:
        direction += "E"
    return direction

def full_word_search(w_map, r, c, direction):

    # Takes search map, row and col of found 'M' and its direction and looks for rest of the XMAS in that direction

    if direction == 'NW':
        if w_map[r-1][c-1] == 'A':
            if w_map[r-2][c-2] == 'S':
                return 1
    elif direction == 'N':
        if w_map[r-1][c] == 'A':
            if w_map[r-2][c] == 'S':
                return 1
    elif direction == 'NE':
        if w_map[r-1][c+1] == 'A':
            if w_map[r-2][c+2] == 'S':
                return 1
    elif direction == 'E':
        if w_map[r][c+1] == 'A':
            if w_map[r][c+2] == 'S':
                return 1
    elif direction == 'W':
        if w_map[r][c-1] == 'A':
            if w_map[r][c-2] == 'S':
                return 1
    elif direction == 'SW':
        if w_map[r+1][c-1] == 'A':
            if w_map[r+2][c-2] == 'S':
                return 1
    elif direction == 'S':
        if w_map[r+1][c] == 'A':
            if w_map[r+2][c] == 'S':
                return 1
    elif direction == 'SE':
        if w_map[r+1][c+1] == 'A':
            if w_map[r+2][c+2] == 'S':
                return 1
    return 0

def word_search(w_map, x_loc):

    # XMAS search function, takes in one location of X as coordinates of row, col and possible map
    # all possible maps listed above as comments
    # Searches for all adjacenet 'M' and the direction the word must be written for legal XMAS 
    # possible directions are NW/N/NE/E/SE/S/SW/W

    Mq = deque()
    counter = 0

    if len(w_map) == 7: # max or tall
        if len(w_map[0]) == 7: # max
            for r in range(2,5): # search for 'M'
                for c in range(2,5):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c , direction])

        else: # tall
            if x_loc == [3, 0]: # left sided
                for r in range(2,5):
                    for c in range (0,2):
                        if w_map[r][c] == 'M':
                            direction = compass(r, c, x_loc)
                            Mq.append([r, c, direction])
            if x_loc == [3, 3]: # right sided
                for r in range(2,5):
                    for c in range(2,4):
                        if w_map[r][c] == 'M':
                            direction = compass(r, c, x_loc)
                            Mq.append([r, c, direction])

    elif len(w_map[0]) == 7: # long
        if x_loc == [0, 3]: # top sided
            for r in range(0,2):
                for c in range(2,5):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])
        if x_loc == [3, 3]: # bottom sided
            for r in range(2,4):
                for c in range(2,5):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])

    else: # min
        if x_loc == [0, 0]: # top left
            for r in range (0,2):
                for c in range(0,2):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])
        if x_loc == [0, 3]: # top right
            for r in range(0,2):
                for c in range(2,4):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])
        
        if x_loc == [3, 0]: # bottom left
            for r in range(2,4):
                for c in range(0,2):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])
        
        if x_loc == [3, 3]: # bottom right
            for r in range(2,4):
                for c in range(2,4):
                    if w_map[r][c] == 'M':
                        direction = compass(r, c, x_loc)
                        Mq.append([r, c, direction])

    while Mq:
        r, c, direction = Mq.popleft()
        counter += full_word_search(w_map, r, c, direction)
    
    return counter

word_map = []
deq = deque()

part_2_q = deque()

answer_1 = 0

for r , line in enumerate(open(input).readlines()):
    line_search = []
    line = str(line.strip('\n'))
    for c, char in enumerate(line):
        line_search.append(char)
        if char == 'X':
            deq.append((r,c))
        if char == 'A':
            part_2_q.append((r,c))

    word_map.append(line_search)

while deq:
    r, c = deq.popleft()
    map_r_start = r-3 if r>= 3 else r
    map_c_start = c-3 if c>= 3 else c
    map_r_end = r+3 if r+3 <= len(word_map) else r
    map_c_end = c+3 if c+3 <= len(word_map[r]) else c
    # make the search map be size of the matrixes at the start

    search_map = list(row[map_c_start:map_c_end+1] for row in word_map[map_r_start:map_r_end+1])

    x_location = [r - map_r_start, c - map_c_start]
    
    answer_1 += word_search(search_map, x_location)

print(f'answer to part1: {answer_1}')

# word_search only takes location of X and word map of possible xmas
# step one is search for adjacent 'M's and create a queue with M and direction the word must be going for legal X M A S
# search for 'A' to follow the 'M' in the legal direction

# PART 2
# X-MAS

answer_2 = 0

def CROSS_MAS_FINDATHON_3000(w_map):
    if w_map[0][0] == 'M' and w_map[2][2] == 'S':
        if w_map[0][2] == 'M' and w_map[2][0] == 'S' or w_map[0][2] == 'S' and w_map[2][0] == 'M':
            return 1
    elif w_map[0][0] == 'S' and w_map[2][2] == 'M':
        if w_map[0][2] == 'M' and w_map[2][0] == 'S' or w_map[0][2] == 'S' and w_map[2][0] == 'M':
            return 1
    return 0

while part_2_q:
    r, c = part_2_q.popleft()
    if r == 0 or c == 0 or r+1 == len(word_map) or c+1 == len(word_map[r]): # 'A' can't be at the edges for valid cross-MAS
        continue
    search_map = list(row[c-1:c+2] for row in word_map[r-1:r+2])
    # A is always in the centre, no need for x_location equivalent
    answer_2 += CROSS_MAS_FINDATHON_3000(search_map)

print(f'answer to part2: {answer_2}')