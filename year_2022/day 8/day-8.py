# inputFile = 'year_2022/day 8/example.txt'
inputFile = 'aoc-inputs/year_2022/day 8/input.txt'

input = open(inputFile, 'r') # real input
#input = open(inputFile, 'r') # example input

def visible_trees_finder(tree_line,forest_x,forest_y):
    
    counter = 0
    x_trigger1 = True
    x_trigger2 = True
    y_trigger1 = True
    y_trigger2 = True

    for x in range(1, forest_x-1):
        for y in range(1, forest_y-1):
            for x_check in range(0, x):
                if tree_line[y][x_check] >= tree_line[y][x]:
                    x_trigger1 = False
                    break
            for x_check in range(x+1, forest_x):
                if tree_line[y][x_check] >= tree_line[y][x]:
                    x_trigger2 = False
                    break
            for y_check in range(0, y):
                if tree_line[y_check][x] >= tree_line[y][x]:
                    y_trigger1 = False
                    break
            for y_check in range(y+1, forest_y):
                if tree_line[y_check][x] >= tree_line[y][x]:
                    y_trigger2 = False
                    break
                
            if (x_trigger1 or x_trigger2 or y_trigger1 or y_trigger2) == True:
                counter += 1
            x_trigger1 = True
            x_trigger2 = True
            y_trigger1 = True
            y_trigger2 = True
    return counter


def tree_house_finder(tree_line, forest_x, forest_y):
    scenic_score = []
    for x in range(0,forest_x):
        for y in range(0,forest_y):
            current_tree = tree_line[x][y]
            left = right = up = down = 0
            for i in range(y - 1, -1, -1):
                left += 1
                if tree_line[x][i] >= current_tree:
                    break
            for i in range(y + 1, len(tree_line[x])):
                right += 1
                if tree_line[x][i] >= current_tree:
                    break
            for i in range(x - 1, -1 , -1):
                up += 1
                if tree_line[i][y] >= current_tree:
                    break
            for i in range (x + 1, len(tree_line[y])):
                down += 1
                if tree_line[i][y] >= current_tree:
                    break
            scenic_score.append(int(left*right*up*down))
    return scenic_score


tree = []
tree_line = []
forest_x = 0
forest_y = 0
forest_x_trigger = False

while True:
    line = input.readline()
    if not line:
        break
    for element in line:
        if element == '\n':
            break
        tree.append(int(element))
        if forest_x_trigger == False:
            forest_x += 1
    
    forest_x_trigger = True
    forest_y += 1
    tree_line.append(tree)
    tree = []

counter = visible_trees_finder(tree_line,forest_x,forest_y)
scenic_score = tree_house_finder(tree_line, forest_x, forest_y)
counter += 2*forest_x + 2*forest_y - 4
print(counter)
print(max(scenic_score))
