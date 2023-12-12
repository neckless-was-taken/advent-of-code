inputFile = 'year_2023/day 7/example.txt'
# inputFile = 'aoc-inputs/year_2023/day 7/input.txt'

# HC - High Card
# 1P - One Pair
# 2P - Two Pair
# 3K - Three of a Kind
# FH - Full House
# 4K - Four of a Kind
# 5k - Five of a Kind

# rankedList - [weakest, ..., strongest]

handsList = []

highCard = []
onePair = []
twoPair = []
threeKind = []
fullHouse = []
fourKind = []
fiveKind = []

def part1(handsList):
    rankedList = []
    for e, hand, bid in enumerate(handsList):
        for card in hand:
            if hand.count(card) == 1:
                highCard.append([hand,bid])
            elif hand.count(card) == 2:
                


for hand in open(inputFile, 'r').readlines():
    cards, bid = hand.strip('\n').split()
    handsList.append([cards,bid])
