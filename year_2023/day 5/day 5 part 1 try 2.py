inputFile = 'year_2023/day 5/example1.txt'
# inputFile = 'aoc-inputs/year_2023/day 5/input.txt'

from tqdm import tqdm
import math

seedMap = {}

def findDivisor(number):
    for i in range(100,1,-1):
        if number % i == 0:
            return i
    return False

def squareMethodWithDivisor(fnseedMap,fnmap,fnfullRangeLength,divisor):
    for i in range(int(fnmap[0]),int(fnmap[0])+fnfullRangeLength+1,int(fnfullRangeLength/divisor)):
        for k,v in fnseedMap.items():
            if i == v:
                print('FOUND IT')
            elif i > v and i > v-fnfullRangeLength:
                newRange = i-int(fnfullRangeLength/divisor)
                for j in tqdm(range(newRange,i)):
                    if v == j:
                        return k, j
                raise ValueError('I should not have gotten here')

def squareMethodNoDivisor(fnseedMap,fnmap,fnfullRangeLength):
    for i in range(int(fnmap[0]),int(fnmap[0])+fnfullRangeLength+10000,10000):
        for k,v in fnseedMap.items():
            if i == v:
                print('FOUND IT')
            elif i>v and i<v-fnfullRangeLength:
                newRange = i-int(fnfullRangeLength/10000)
                for j in tqdm(range(newRange,i)):
                    if v == j:
                        return k,j
                raise ValueError('ruh-roh') 
        
def getSeedKey(seedMap, searchMap):
    for k,v in seedMap.items():
        if v == searchMap:
            return k

input = []
for line in open(inputFile, 'r').readlines():
    input.append(line.strip('\n'))

for n in range(len(input)):
    if 'seeds' in input[n]:
        seeds = []
        while True:
            seeds.append(input[n])
            n += 1
            if input[n] == '':
                seeds[0] = seeds[0].split(': ')[1]
                for i in seeds[0].split():
                    seedMap[i] = int(i)
                break
            else:
                continue
    if input[n] == '' or ':' in input[n]:
        continue
    
    inputMap = input[n].split()
    # updatedKeys = []
    # for i in tqdm(range(int(map[-1]))):
    #     if int(map[1])+i in seedMap.values():
    #         key = getSeedKey(seedMap, int(map[1])+i)
    #         if key not in updatedKeys:
    #             if key == '14':
    #                 pass
    #             updatedKeys.append(key)
    #             seedMap[key] = int(map[0])+i

    fullRangeLength = int(inputMap[2])
    updatedKeys = []
    for k,v in seedMap.items():
        if k in updatedKeys:
            continue
        else:
            if v < fullRangeLength or v > fullRangeLength:
                div = findDivisor(fullRangeLength)
                if div != False and div != 0 and div != '0':
                    key, newValue = squareMethodWithDivisor(seedMap,inputMap,fullRangeLength,div)
                    updatedKeys.append(key)
                    seedMap[key] = int(inputMap[0])+newValue
                else:
                    key, newValue = squareMethodNoDivisor(seedMap,inputMap,fullRangeLength)
                    updatedKeys.append(key)
                    seedMap[key] = int(inputMap[0])+newValue


# print(min(seedMap.values()))
print(seedMap)