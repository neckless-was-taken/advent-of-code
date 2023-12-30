# revisit date: 27/12/2023

inputFile = 'year_2022/day 6/example.txt'
inputFile = 'aoc-inputs/year_2022/day 6/input.txt'

message = open(inputFile).read().strip('\n').strip()

def message_marker(x, message):

    def counter(substring):
        char_count = {}
        for ch in substring:
            if ch in char_count:
                return False
            else:
                char_count[ch] = 1
        return True

    for i in range(0,len(message)):
        for ch in message[i:x+i]:
            if counter(message[i:x+i]):
                return i+x
            else:
                continue          
    raise RuntimeError()

print(f'part 1: {message_marker(4, message)}')
print(f'part 2: {message_marker(14, message)}')
