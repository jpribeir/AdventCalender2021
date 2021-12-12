# Day 12 of the 2021 Advent of Code
class Cave():
    # Initiate the object
    def __init__(self,name,connect):
        self.name = name
        self.connect_list = []
        self.addConnect(connect)
        
    def addConnect(self,connect):
        self.connect_list.append(connect)

# Convert input to a list of objects
def OLDfile2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    cave_list = []
    for line in input_list:
        caveA = line.strip().split("-")[0]
        caveB = line.strip().split("-")[1]
        checkedA = False
        checkedB = False
        for i,cave in enumerate(cave_list):
            if cave.name==caveA:
                cave.addConnect(caveB)
                checkedA = True
            elif cave.name==caveB:
                cave.addConnect(caveA)
                checkedB = True
        if not checkedA: cave_list.append(Cave(caveA,caveB))
        if not checkedB: cave_list.append(Cave(caveB,caveA))
    return cave_list

# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    cave_dict = {}
    for line in input_list:
        caveA = line.strip().split("-")[0]
        caveB = line.strip().split("-")[1]
        checkedA = False
        checkedB = False
        for cave in cave_dict:
            if cave==caveA:
                cave_dict[cave].append(caveB)
                checkedA = True
            elif cave==caveB:
                cave_dict[cave].append(caveA)
                checkedB = True
            if checkedA and checkedB: break
        else:
            if not checkedA: cave_dict[caveA] = [caveB]
            if not checkedB: cave_dict[caveB] = [caveA]
    return cave_dict

def enterCave(here,cave_dict):
    for

def part1(cave_dict):
    return enterCave("start",cave_dict)

# Read input file
cave_dict = file2list("../include/input12.inc")
for cave in cave_dict:
    print(cave)
    print(cave_dict[cave])
example_list = file2list("../include/example12.inc")
#path_count = part1(cave_list)
#print("----DAY 12----\nPart1: %s"%part1(example_list))
#print("Part2: %s"%part2(out_map,100))