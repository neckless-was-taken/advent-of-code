# input = 'year_2022/day 17/example.txt'
input = 'aoc-inputs/year_2022/day 17/input.txt'

jets = [line for line in open(input).readline()]

rocks = [[['.','.','@','@','@','@','.']],[['.','.','.','@','.','.','.'],['.','.','@','@','@','.','.'],['.','.','.','@','.','.','.']],[['.','.','.','.','@','.','.'],['.','.','.','.','@','.','.'],['.','.','@','@','@','.','.']],[['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.']],[['.','.','@','@','.','.','.'],['.','.','@','@','.','.','.']]]
chamber = [['-','-','-','-','-','-','-']]
airgap = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
air = ['.','.','.','.','.','.','.']


ri = 0
ji = 0

# print('rock formations: ')
# for e, i in enumerate(rocks):
#     x = len(rocks[e])
#     if len(rocks[e]) < 6:
#         for j in i:
#             for k in j:
#                 print(k,end='')
#             print()
#             # print(j,end='')
#         print()
#     else:
#         for j in i:
#             print(j,end='')
#         print()
#         print()


def f(chamber, jets, rock):
    air = ['.','.','.','.','.','.','.']
    airgap = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
    for this_is_gay in airgap:
        chamber.append(this_is_gay)
    r_edge = False
    l_edge = False
    fallen = False
    ji = 0
    # jet = '<'

    for i in range(0,len(rock)):
        chamber.append(rock[-1-i])

    while True:
        # if jet == '>':
        #     for i in range(0,len(rock)):
        #         if not edge:
        #             chamber[-1-i].pop(-1)
        #             chamber[-1-i].insert(0,'.')
        #     for i in (i for i in range(0,len(rock)) if chamber[-1-i][6] != '.'):
        #         edge = True
        # elif jet == '<':
        #     for i in range(0,len(rock)):
        #         if not edge:
        #             chamber[-1-i].pop(0)
        #             chamber[-1-i].append('.')
        #     for i in (i for i in range(0,len(rock)) if chamber[-1-i][0] != '!'):
        #         edge = True

        if ji < len(jets):
            jet = jets[ji]
            ji += 1
        else:
            ji = 0

        if jet == '>':
            vis = []
            for i in range(1,len(chamber)):
                if '@' in chamber[i]:
                    if chamber[i][6] == '@':
                        r_edge = True
                        break
                    else:
                        for j in range(2,7):
                            if j not in vis:
                                if chamber[i][-j+1] == '.':
                                    break

                if r_edge:
                    break
            if not r_edge:
                for i in range(1,len(chamber)):
                    if '@' in chamber[i] and chamber[i][6] != '@':
                        for j in range(2,7):
                            if chamber[i][-j] == '@':
                                chamber[i][-j+1] = '@'
                                chamber[i][-j] = '.'


        if jet == '<':
            vis = []
            for i in range(1,len(chamber)):
                if '@' in chamber[i]:
                    if chamber[i][0] == '@':
                        l_edge = True
                        break
                    else:
                        for j in range(1,6):
                            if j not in vis:
                                if chamber[i][j-1] == '.':
                                    break

                if l_edge:
                    break
            if not l_edge:
                for i in range(1,len(chamber)):
                    if '@' in chamber[i] and chamber[i][0] != '@':
                        for j in range(1,6):
                            if chamber[i][j] == '@':
                                chamber[i][j-1] = '@'
                                chamber[i][j] = '.'

        vis = []
        l = len(rock)
        if len(chamber) > 1:
            for i in range(0,len(chamber)):
                if '@' in chamber[1]:
                    fallen = True
                else:
                    for j in range(0,7):
                        if chamber[i][j] == '@':
                            if j not in vis:
                                vis.append(j)
                                if chamber[i-1][j] != '.':
                                    fallen = True
                                    break
                if fallen:
                    break

        if not fallen and len(chamber) > 1:
            for i in range(1,len(chamber)):
                for j in range(0,7):
                    if chamber[i][j] == '@':
                        if chamber[i-1][j] == '.':
                            chamber[i-1][j] = '@'
                            chamber[i][j] = '.'
            if chamber[-1] == air:
                for _ in range(0,len(chamber[-1])):
                    chamber[-1].remove(chamber[-1][0])
                chamber.pop(-1)
        else:
            break

    for i in range(0,len(chamber)):
        for j in range(0,len(chamber[i])):
            if chamber[i][j] == '@':
                chamber[i][j] = '#'

    return chamber


for index in range(0,2022):
    if ri < len(rocks):
        rock = list(rocks[ri])
        ri += 1
    else:
        ri = 0
        rock = list(rocks[ri])
    rocks = [[['.','.','@','@','@','@','.']],[['.','.','.','@','.','.','.'],['.','.','@','@','@','.','.'],['.','.','.','@','.','.','.']],[['.','.','.','.','@','.','.'],['.','.','.','.','@','.','.'],['.','.','@','@','@','.','.']],[['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.']],[['.','.','@','@','.','.','.'],['.','.','@','@','.','.','.']]]
    chamber = f(chamber, jets, rock)
    print('running index :',index)
    # print()
    # print('chamber: ')

    # for i in chamber:
    #     for j in i:
    #         print(j,end='')
    #     print()

    pass
print()
print()
print('chamber: ')
chamber.reverse()
for e,i in enumerate(chamber):
    print(e,' ',end='')
    for j in i:
        print(j,end='')
    print()

print('the tower is :',len(chamber),'units tall')


## todo
## something wrong
## rock no finish fall