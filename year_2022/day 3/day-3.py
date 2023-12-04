answer1 = 0
answer2 = 0
rucksack=''
alphabet=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# inputFile = 'year_2022/day 3/example.txt'
inputFile = 'aoc-inputs/year_2022/day 3/input.txt'

input = open(inputFile,'r') # example input

#while True:
#    current_item_index=0
#    answer1_trigger = False
#    compartment1=''
#    compartment2=''
#    rucksack = list(input.readline())
#    if not rucksack:
#        break
#    compartment_size = len(rucksack) // 2
#    while current_item_index != compartment_size:
#        compartment1 += str(rucksack[current_item_index])
#        current_item_index += 1
#    while current_item_index != len(rucksack):
#        current_item = str(rucksack[current_item_index])
#        compartment2 += current_item
#        if answer1_trigger == False:
#            if current_item in compartment1:
#                answer1_trigger = True
#                #print(alphabet.index(current_item)+1)
#                answer1 += alphabet.index(current_item)+1                       
#            else:
#                pass
#        else:
#            break
#        current_item_index += 1
#    #print('first compartment : '+compartment1+' second compartment = '+compartment2)
#print(answer1)

## PART TWO

current_rucksack_index = 0
group = ''
current_item=[]
rucksack2=['','','']

while True:
    if current_rucksack_index != 3:
        rucksack2[current_rucksack_index] = input.readline()
        if not rucksack2[current_rucksack_index]:
            break
        if current_rucksack_index == 2:
            #todo see if any rucksack 3 letters are in rucksacks 1 AND 2
            #todo seperate rucksacks into rucksack[0] rucksack[1] and rucksack[2] as a list rucksack[i]
            #todo walk through rucksack[2] letter by letter and compare if in rucksack[0] and rucksack[1]
            current_item_index = 0
            while current_item_index != len(rucksack2[current_rucksack_index])+1:
                current_item[current_item_index] = list(rucksack2[current_rucksack_index])
            pass
        current_rucksack_index += 1
    else:
        current_rucksack_index = 1