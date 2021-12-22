# Day 22 of the 2021 Advent of Code
class Instruction():
    # Initiate the object
    def __init__(self,action,coord_list):
        self.action = action
        self.xrange = list(range(coord_list[0],coord_list[1]+1))
        self.yrange = list(range(coord_list[2],coord_list[3]+1))
        self.zrange = list(range(coord_list[4],coord_list[5]+1))

# Convert input to a list
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        lines_list =  list(map(lambda x: x.strip(),input_file.readlines()))
    maxval = 0
    instruction_list = []
    for line in lines_list:
        action = line.split(" ")[0]
        range_list = line.split(" ")[1].split(",")
        coord_list = []
        for line in range_list:
            coord_list.append(int(line.split("=")[1].split("..")[0]))
            coord_list.append(int(line.split("=")[1].split("..")[1]))
        maxval = max(maxval,max(coord_list))
        instruction_list.append(Instruction(action,coord_list))
    for each in instruction_list:
        each.xrange = list(map(lambda x: x+maxval,each.xrange))
        each.yrange = list(map(lambda x: x+maxval,each.yrange))
        each.zrange = list(map(lambda x: x+maxval,each.zrange))
    return instruction_list,maxval

def part1(instruction_list,maxval):
    cube_grid = [[[0 for x in range(-maxval,maxval+1)] for y in range(-maxval,maxval+1)] for z in range(-maxval,maxval+1)]
    i = 0
    for each in instruction_list:
        i +=1
        print(i)
        for x in each.xrange:
            for y in each.yrange:
                for z in each.zrange:
                    if each.action=="on": cube_grid[x][y][z] = 1
                    else: cube_grid[x][y][z] = 0
    on_count = 0
    for x in cube_grid:
        for y in x: on_count += y.count(1)
    return on_count

# Read input file
instruction_list,maxval = file2list("../include/input22.inc")
example_list,example_maxval = file2list("../include/example22.inc")
print("----DAY 22----\nPart1: %s"%part1(example_list))
print("Part2: %s"%part1(instruction_list,maxval))