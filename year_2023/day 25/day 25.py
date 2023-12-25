# this solution is from: https://www.youtube.com/watch?v=S_rdenmcsm8

# inputFile = 'year_2023/day 25/example.txt'
inputFile = 'aoc-inputs/year_2023/day 25/input.txt'

import networkx as nx 

g = nx.Graph()

for line in open(inputFile):
    left, right = line.split(':')
    for node in right.strip().split():
        g.add_edge(left, node)
    
g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a)*len(b))