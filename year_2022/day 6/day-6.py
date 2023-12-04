# inputFile = 'year_2022/day 6/example.txt'
inputFile = 'aoc-inputs/year_2022/day 6/input.txt'

#input = open(inputFile, 'r') # real input
input = open(inputFile, 'r') # example input

input=input.readline()
input_signal=list(input)
received_signal = []

for received_character in input:
    received_signal.append(received_character)


def marker_finder(received_signal, first, second, third, fourth):
    #print(received_signal[first], received_signal[second],received_signal[third],received_signal[fourth])
    if received_signal[first] in received_signal[second]:
        print('return 1')
        return 0
    else:
        if received_signal[first] in received_signal[third]:
            print('return 2')
            return 0
        else:
            if received_signal[first] in received_signal[fourth]:
                print('return 3')
                return 0
            else:
                if received_signal[second] in received_signal[third]:
                    print('return 4')
                    return 0
                else:
                    if received_signal[second] in received_signal[fourth]:
                        print('return 5')
                        return 0
                    else:
                        if received_signal[third] in received_signal[fourth]:
                            print('return 5')
                            return 0
                        else:
                            print('final return')
                            return fourth

start = 0
end = 13

def message_finder(received_signal, end):
    start = end - 13
    for current_start in range(start,end):
        for current_next in range(current_start,end):
            if received_signal[current_start] in received_signal[current_next]:
                pass
            #todo figure this shit out hehe
                


## PART 1

first = 0
second = 1
third = 2
fourth = 3

answer2 = 0
answer2_trigger = False
i = 13

#print(len(received_signal))

#for _ in range(0,len(received_signal)-3):
#    answer1 = marker_finder(received_signal, first, second, third, fourth)
#    if answer1 != 0:
#        break
#    first += 1
#    second += 1
#    third += 1
#    fourth += 1
#print(answer1+1)

## PART 2

for _ in range(0,len(received_signal)):
    message_finder(received_signal, i)
    if answer2 == True:
        print('this return 5')
        break

print(answer2)
print(i)
