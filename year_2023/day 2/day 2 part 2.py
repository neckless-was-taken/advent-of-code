# input = 'year_2023/day 2/example1.txt'
input = 'aoc-inputs/year_2023/day 2/input.txt'

power = 0

for line in open(input).readlines():
    lowestCubes = {}
    gameID = int(line.strip('Game ').split(":")[0])
    gameHints = str(line.strip('Game ').strip('\n').split(":")[-1]).split(';')
    for subset in gameHints:
        subset = subset.split(',')
        for cubes in subset:
            cubes = cubes.strip().split(' ')
            try:
                if int(cubes[0]) > int(lowestCubes.get(cubes[-1])):
                    lowestCubes.update({cubes[1]:int(cubes[0])})
            except TypeError:
                lowestCubes.update({cubes[1]:int(cubes[0])})
    power += lowestCubes.get('blue')*lowestCubes.get('red')*lowestCubes.get('green')
print(power)