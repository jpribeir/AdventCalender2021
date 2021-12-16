# Day 15 of the 2021 Advent of Code
class Position():
    # Initiate the object
    def __init__(self,i,j,risk,neighbour_list):
        self.i,self.j = i,j
        self.visited = False
        self.risk = risk
        self.path_cost = float("inf")
        self.neighbour_list = neighbour_list

# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return [[int(num) for num in line.strip()] for line in input_file.readlines()]

# This implementetion only works for the first part since it assumes the path will always go right and down
def part1(risk_map):
    # Each position is its cost plus the min of the cost from the two previous possible positions
    cost_list = [[0 for j in range(len(risk_map[0]))] for i in range(len(risk_map))]
    for i in range(1,len(risk_map)):
        cost_list[i][0] = risk_map[i][0] + cost_list[i-1][0]
    for j in range(1,len(risk_map[0])):
        cost_list[0][j] = risk_map[0][j] + cost_list[0][j-1]
    for i in range(1,len(risk_map)):
        for j in range(1,len(risk_map[0])):
            cost_list[i][j] = min(cost_list[i][j-1],cost_list[i-1][j]) + risk_map[i][j]
    return cost_list[-1][-1]

def extendMap(risk_map,extend):
    extended_map = risk_map
    # First, extend each line 4 times to the right
    for i,line in enumerate(risk_map):
        copy_list = line
        for time in range(1,extend):
            aux_list = list(map(lambda a: a+1 if a<9 else 1, copy_list))
            extended_map[i] = extended_map[i] + aux_list
            copy_list = aux_list
    # Second, extend all lines 4 times down
    for time in range(1,extend):
        extension_list = []
        for line in extended_map[(time-1)*len(risk_map):]:
            aux_list = list(map(lambda a: a+1 if a<9 else 1, line))
            extension_list.append(aux_list)
        extended_map = extended_map + extension_list
    return extended_map

def part2(risk_map):
    imax = len(risk_map)
    jmax = len(risk_map[0])
    # Create a dictionary of all points with its info and list of neighbours
    pos_dict = {}
    for i,line in enumerate(risk_map):
        for j,num in enumerate(line):
            neighbour_list = []
            for m,n in [(-1,0),(0,-1),(0,1),(1,0)]:
                if i+m in range(imax) and j+n in range(jmax): neighbour_list.append((i+m,j+n))
            pos_dict[(i,j)] = Position(i,j,num,neighbour_list)
    # First point is the only known cost, once a point has a cost different from infinity, it coes in the unvisited stack
    pos_dict[(0,0)].path_cost = 0   
    unvisited_dict = {(0,0): 0}
    while True:
        # Search the closest point that had a cost already calculated
        i,j = min(unvisited_dict, key=unvisited_dict.get)
        # In case the destination was visited the answer is found
        if (i,j)==(imax-1,jmax-1): return pos_dict[(i,j)].path_cost
        for m,n in pos_dict[(i,j)].neighbour_list:
            # If the neighbour wasn't yet visited, check if its cost can be lowered and update it
            if not pos_dict[(m,n)].visited:
                pos_dict[(m,n)].path_cost = min(pos_dict[(m,n)].path_cost,pos_dict[(i,j)].path_cost + pos_dict[(m,n)].risk)
                unvisited_dict[(m,n)] = pos_dict[(m,n)].path_cost
        # After the current point is visted, remove it from the searchable queue
        pos_dict[(i,j)].visited = True
        del unvisited_dict[(i,j)]

# Read input file
risk_map = file2list("../include/input15.inc")
print("----DAY 15----\nPart1: %s"%part1(risk_map))
print("Part2: %s"%part2(extendMap(risk_map,5)))