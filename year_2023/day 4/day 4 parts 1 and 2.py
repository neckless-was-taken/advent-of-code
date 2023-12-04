# inputFile = 'year_2023/day 4/example1.txt'
inputFile = 'aoc-inputs/year_2023/day 4/input.txt'

part1 = 0
part2 = 0
winningCardCount = {}
cardCount = {}
cards = []

input = open(inputFile, 'r')
for line in input.readlines():
    cards.append(line.strip('\n'))
    cardID = int(line.split(': ')[0].split()[1])
    cardCount[cardID] = 1
input.close()

def part2calc(winningCardCount,cardCount):
    for n,matches in winningCardCount.items():
        if matches > 0:
            for i in range(n+1,n+matches+1):
                for j in range(0,cardCount.get(n)):
                    cardCount[i] += 1
    return cardCount

for card in cards:
    cardID = int(card.split(': ')[0].split()[1])
    gameNumbers = card.split(': ')[-1].split(' | ')
    winningNumbers = gameNumbers[0].split()
    myNumbers = gameNumbers[1].split()
    matchingNumbers = 0
    for num in myNumbers:
        if num in winningNumbers:
            matchingNumbers += 1
    winningCardCount[cardID] = matchingNumbers
    if matchingNumbers > 0:
        score = 2**(matchingNumbers-1)
    else:
        score = 0
    part1 += score
cardCount = part2calc(winningCardCount,cardCount)
for k,v in cardCount.items():
    part2 += v

print(f'part 1 = {part1}')
print(f'part 2 = {part2}')