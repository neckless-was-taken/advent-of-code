# input = 'year_2024/day 9/example.txt'
input = 'aoc-inputs/year_2024/day 9/input.txt'

from tqdm import tqdm

for line in open(input).readlines():
    line = str(line.strip('\n'))

disk = []
x = 0 # id

for e, i in enumerate(line):
    if e == 0 or e % 2 == 0:
        # file
        for j in range(int(i)):
            disk.append(x)
        x += 1
    else:
        # empty space
        for j in range(int(i)):
            disk.append('.')

done = False
last_id = 0 # last time this was the first empty space, search from here
while True:
    if disk[-1] == '.':
        disk.pop()
        continue
    len_disk = len(disk)-1
    to_move = disk.pop()
    for i in range(last_id,len_disk+1):
        try:
            if disk[i] == '.':
                disk[i] = to_move
                last_id = i
                break
        except IndexError:
            disk.append(to_move)
            done = True
            break
    if done:
        break

answer_1 = 0

for e, i in enumerate(disk):
    answer_1 += e*i

print(f'answer to part 1: {answer_1}')


# part 2

def space_saver3000(space,file):
    size = len(file)
    available = 0
    new_file = []
    for e, i in enumerate(space):
        if i == '.':
            available += 1
            if available == size:
                for j in space[0:e-size+1]:
                    new_file.append(j)
                for j in file:
                    new_file.append(j)
                if len(new_file) < len(space):
                    for j in space[e+size-1:]:
                        new_file.append(j)
                return new_file
        else:
            available = 0
    return 0

for line in open(input).readlines():
    line = str(line.strip('\n'))

disk = []
x = 0 # id

for e, i in enumerate(line):
    if e == 0 or e % 2 == 0:
        file = []
        # file
        for j in range(int(i)):
            file.append(x)
        disk.append(file)
        x += 1
    else:
        # empty space
        empty = []
        for j in range(int(i)):
            empty.append('.')
        if empty:
            disk.append(empty)


new_disk = []
length = len(disk)

for files in disk:

    new_disk.append(files)

for i in tqdm(range(len(disk))):
    files = disk.pop()
    if '.' in files:
        continue

    for e, check in enumerate(new_disk):
        if e+1 >= length-i:
            break
        if '.' in check:
            if len(files) <= len(check):
                saver = space_saver3000(check, files)
                if saver:
                    new_disk[e] = saver
                    fmoved = new_disk[length-i-1]
                    free_space = []
                    for j in fmoved:
                        free_space.append('.')
                    new_disk[length-i-1] = free_space
                    # print(f'moved file: {fmoved} to {saver}, now location {length-i-1} contains {new_disk[length-i-1]}')
                    break
    # else:
    #     disk.append(files)
# print(new_disk)

fdisk = []
answer_2 = 0

for i in new_disk:
    for j in i:
        fdisk.append(j)

for e, i in enumerate(fdisk):
    if i != '.':
        answer_2 += e * int(i)
    
tfdisk = []
unbroken = 1

for i in fdisk[::-1]:
    if unbroken:
        if i == '.':
            continue
        else:
            unbroken = 0
    else:
        tfdisk.append(i)

trimmed_fdisk = tfdisk[::-1]

print(f'answer to part 2: {answer_2}')
print(f"sadly this isn't correct :(, the solution to my input is 'too high'")
