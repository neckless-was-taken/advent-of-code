input = 'year_2024/day 22/example.txt'
input = 'aoc-inputs/year_2024/day 22/input.txt'

from tqdm import tqdm

def part_1(s = int):
    value = s * 64
    s = mix_n_prune(value, s)
    value = int(str(s / 32).split('.')[0])
    s = mix_n_prune(value, s)
    value = s * 2048
    s = mix_n_prune(value, s)
    return s

def mix_n_prune(v = int, s = int):
    s = v ^ s
    return s % 16777216

def p_2_brute():
    abcd = []
    s = -9
    b = 10
    for a in range(s,b):
        for b in range(s,b):
            for c in range(s,b):
                for d in range(s,b):
                    abcd.append([a,b,c,d])
    return abcd

answer_1 = 0
m_prices = []
m_deltas = []

for line in tqdm(open(input).readlines()):
    line = int(line.strip('\n'))
    # line = 123
    secret = line
    prices = []
    deltas = []
    prices.append(int(str(secret)[-1]))
    deltas.append(0)
    most = 0
    for _ in range(2000):
        secret = part_1(secret)
        # part 2
        x = int(str(secret)[-1])
        deltas.append(x - prices[-1])
        prices.append(x)
        most = x if most < x else most
    # for x in part_2:
    #     print(x)
    # print(most)
    m_prices.append(prices)
    m_deltas.append(deltas)


    answer_1 += secret
    # break

print(answer_1)
# for i in range(len(m_prices)):
#     print(m_prices[i],max(m_prices[i]))
#     print(m_deltas[i])
#     break

possible_answers = []
answer_2 = 0
x = 0

abcd_list = p_2_brute()

for abcd in tqdm(abcd_list):

    abcd = [1, -3, 5, 1]
    for i,deltas in enumerate(m_deltas):
        for j in range(1,len(deltas)-4):
            if deltas[j:j+4] == abcd:
                try:
                    x += m_prices[i][j+4]
                    # print(m_prices[i][j:j+4],m_deltas[i][j:j+4])
                except:
                    pass
                break
    possible_answers.append(x)
    # if x == 23 or x == 24 or x == 25:
    #     print(abcd, x)
    x = 0

print(f'max = {max(possible_answers)}')
print(f'top 5:')
top_5 = sorted((set(possible_answers)), reverse=True)[:5]
for i,x in enumerate(top_5):
    print(f'{abs(i+1)}: {x}')