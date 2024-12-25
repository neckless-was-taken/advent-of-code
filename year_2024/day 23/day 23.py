input = 'year_2024/day 23/example.txt'
# input = 'aoc-inputs/year_2024/day 23/input.txt'

from tqdm import tqdm

# part 2
def most_popular(comps):
    computers = []
    for x in comps:
        computers.extend(x)
    
    count = {}
    for x in computers:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    most = None
    counter = 0
    for k, v in count.items():
        if v > counter:
            most = k
            counter = v
    
    return most, counter
# 

computers = []

for line in open(input).readlines():
    computers.append(list(str(line.lower().strip('\n')).split('-')))

# part 1
lan = []

for e, ab in tqdm(enumerate(computers)):
    a,b = ab[0], ab[1]
    for cd in computers[e+1:]:
        c = 0
        x = -1
        if a in cd:
            if a == cd[0]:
                c = cd[1]
                x = 0
            elif a == cd[1]:
                c = cd[0]
                x = 1
        if b in cd:
            if b == cd[0]:
                c = cd[1]
                x = 0
            elif b == cd[1]:
                c = cd[0]
                x = 1
        if c and x != -1:
            for ef in computers:
                if c in ef and ab[x] in ef:
                    if ef == cd:
                        continue
                    lan.append(tuple(sorted((a,b,c))))
lan = set(lan)

answer_1 = 0

for abc in lan:
    a,b,c = abc[0],abc[1],abc[2]
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        answer_1 += 1
        continue

print(f'answer to part 1: {answer_1}')
# end part 1


# part 2
# My part 2 solution assumes that the most popular PC will be only connected to the largest LAN and not any other computers
# My assumption was correct

likely, count = most_popular(lan)

likely_lan = []
for abc in lan:
    if likely in abc:
        likely_lan.extend(abc)
likely_lan = sorted(set(likely_lan))

answer_2 = ''
for x in likely_lan:
    if not answer_2:
        answer_2 = str(x)
    else:
        answer_2 += ','+str(x)

print(f'answer to part 2: {answer_2}')