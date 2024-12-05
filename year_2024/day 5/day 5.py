input = 'year_2024/day 5/example.txt'
# input = 'aoc-inputs/year_2024/day 5/input.txt'

def wrong_list_finder3000(rule):
    for r, row in enumerate(page_numbers):
        if wrong_lists[r] == 1:
            continue
        if rule[0] in row:
            if rule[1] in row[:row.index(rule[0])]:
                wrong_lists[r] = 1
                continue
    return

starts = []
ends = []

global wrong_lists, page_numbers, rules
rules = []
page_numbers = []
wrong_lists = []

for line in open(input).readlines():
    line = str(line.strip('\n'))
    if "|" in line:
        rules.append(line.split('|'))
        starts.append(line.split('|')[0])
        ends.append(line.split('|')[-1])
        wrong_lists.append(0)

    elif "," in line:
        page_numbers.append(line.split(','))

answer_1 = 0

for r in rules:
    wrong_list_finder3000(r)

for i in range(len(page_numbers)):
    if wrong_lists[i] == 0:
        answer_1 += int(page_numbers[i][int(len(page_numbers[i])/2)])

print(f'answer to part 1: {answer_1}')
print()

# PART 2

answer_2 = 0

def page_sorter3000(page):
    # figure out how to sort it

    return int(page[int(len(page)/2)])


wrong_pages = []

for e, l in enumerate(page_numbers):
    if wrong_lists[e] == 1:
        wrong_pages.append(page_numbers[e])

for p in wrong_pages:
    answer_2 += page_sorter3000(p)

print(f'answer to part 2: {answer_2}')
print()