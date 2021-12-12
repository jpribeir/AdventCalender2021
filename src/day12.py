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

def enterCave(here,cave_dict,visited_list):
    path_count = 0
    print(visited_list)
    for cave in cave_dict[here]:
        if cave.isupper():
            aux_list = visited_list.copy()
            aux_list.append(cave)
            path_count += enterCave(cave,cave_dict,aux_list)
        elif cave.islower():
            if cave=="end":
                return 1
            elif cave not in visited_list:
                aux_list = visited_list.copy()
                aux_list.append(cave)
                path_count += enterCave(cave,cave_dict,aux_list)
                visited_list = aux_list.copy()
    return path_count

def part1(cave_dict):
    return enterCave("start",cave_dict,["start"])

# Read input file
cave_dict = file2list("../include/input12.inc")
#example_list = file2list("../include/example12.inc")
print("----DAY 12----\nPart1: %s"%part1(cave_dict))
#print("Part2: %s"%part2(out_map,100))