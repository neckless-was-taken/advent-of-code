inputFile = 'year_2023/day 5/example1.txt'
# inputFile = 'aoc-inputs/year_2023/day 5/input.txt'

seeds = []
seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humiditiyToLocation = []

input = []
for line in open(inputFile, 'r').readlines():
    input.append(line.strip('\n'))

for i in range(0,len(input)-1):
    if 'seeds' in input[i]:
        while True:
            seeds.append(input[i])
            i += 1
            if input[i] == '':
                seeds[0] = seeds[0].split(': ')[1]
                break
            else:
                continue
    
    if 'seed-to-soil' in input[i]:
        while True:
            seedToSoil.append(input[i])
            i += 1
            if input[i] == '':
                seedToSoil.pop(0)
                break
            else:
                continue

    if 'soil-to-fertilizer' in input[i]:
        while True:
            soilToFertilizer.append(input[i])
            i += 1
            if input[i] == '':
                soilToFertilizer.pop(0)
                break
            else:
                continue
    
    if 'fertilizer-to-water' in input[i]:
        while True:
            fertilizerToWater.append(input[i])
            i += 1
            if input[i] == '':
                fertilizerToWater.pop(0)
                break
            else:
                continue

    if 'water-to-light' in input[i]:
        while True:
            waterToLight.append(input[i])
            i += 1
            if input[i] == '':
                waterToLight.pop(0)
                break
            else:
                continue
    
    if 'light-to-temperature' in input[i]:
        while True:
            lightToTemperature.append(input[i])
            i += 1
            if input[i] == '':
                lightToTemperature.pop(0)
                break
            else:
                continue

    if 'temperature-to-humidity' in input[i]:
        while True:
            temperatureToHumidity.append(input[i])
            i += 1
            if input[i] == '':
                temperatureToHumidity.pop(0)
                break
            else:
                continue

    if 'humidity-to-location' in input[i]:
        while True:
            humiditiyToLocation.append(input[i])
            i += 1
            if i >= len(input) or input[i] == '':
                humiditiyToLocation.pop(0)
                break
            else:
                continue

pass