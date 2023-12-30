inputFile = 'year_2023/day 18/example.txt'
# inputFile = 'aoc-inputs/year_2023/day 18/input.txt'

import time
start_t = time.time()

trench = []

for line in open(inputFile).readlines():
    direction, distance, *colour = line.split()
    

end_t = time.time()
print(f'total time: {end_t-start_t}')