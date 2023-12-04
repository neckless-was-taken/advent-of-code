# input = 'year_2023/day 2/example1.txt'
input = 'aoc-inputs/year_2023/day 2/input.txt'

gameRules = {'red':12,'green':13,'blue':14}

possibleGames = 0

for line in open(input).readlines():
    impossible = False
    gameID = int(line.strip('Game ').split(":")[0])
    gameHints = str(line.strip('Game ').strip('\n').split(":")[-1]).split(';')
    for subset in gameHints:
        subset = subset.split(',')
        for cubes in subset:
            cubes = cubes.strip().split(' ')
            if int(cubes[0]) > gameRules.get(cubes[-1]):
                impossible = True
                break
        if impossible:
            break
    if impossible:
        continue
    possibleGames += gameID
print(possibleGames)