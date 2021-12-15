# Day 15 of the 2021 Advent of Code
# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return [[int(num) for num in line.strip()] for line in input_file.readlines()]

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
    for i,line in enumerate(risk_map):
        copy_list = line
        for time in range(1,extend):
            aux_list = list(map(lambda a: a+1 if a<9 else 1, copy_list))
            extended_map[i] = extended_map[i] + aux_list
            copy_list = aux_list
    for time in range(1,extend):
        extension_list = []
        for line in extended_map[(time-1)*len(risk_map):]:
            aux_list = list(map(lambda a: a+1 if a<9 else 1, line))
            extension_list.append(aux_list)
        extended_map = extended_map + extension_list
    return extended_map

def visitNum(i,j,risk_map,cost_map,visited_map):
    visited_map[i][j] = True
    if i==len(risk_map)-1 and j==len(risk_map)[0]:
        return cost_map
    for m,n in [(-1,0),(0,-1),(0,1),(1,0)]:
        if i+m in range(len(risk_map)) and j+n in range(len(risk_map[0])):
            if not visited_map[i+m][j+n]:
                cost_map[i+m][j+n] = min(cost_map[i+m][j+n],cost_map[i][j] + risk_map[i+m][j+n])
    return visitNum(x,y,risk_map,cost_map,visited_map)

def part2(risk_map):
    imax = len(risk_map)
    jmax = len(risk_map[0])
    cost_map = [[float("inf") for j in range(jmax)] for i in range(imax)]
    unvisited_list = [(i,j) for i in range(imax) for j in range(jmax)]
    cost_map[0][0] = 0
    #paths_cost_map = visitNum(0,0,risk_map,cost_map,visited_map)
    i,j = 0,0
    while True:
        #print(len(unvisited_list))
        try:
            i,j = unvisited_list[min([min(n[j-5:j+5]) for n in cost_map[i-5:i+5]])]
        except:
            i,j = unvisited_list[min([min(n) for n in cost_map])]
        if (i,j)==(imax-1,jmax-1): return cost_map[i][j]
        for m,n in [(-1,0),(0,-1),(0,1),(1,0)]:
            try:
                if (i+m,j+n) in unvisited_list:
                    cost_map[i+m][j+n] = min(cost_map[i+m][j+n],cost_map[i][j] + risk_map[i+m][j+n])
            except:
                pass
        unvisited_list.remove((i,j))

# Read input file
risk_map = file2list("../include/input15.inc")
example_map = file2list("../include/example15.inc")
#print("----DAY 15----\nPart1: %s"%part1(risk_map))
print("Part2: %s"%part2(extendMap(risk_map,5)))