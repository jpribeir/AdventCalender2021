# Day 12 of the 2021 Advent of Code
# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    cave_dict = {}
    for line in input_list:
        caveA = line.strip().split("-")[0]
        caveB = line.strip().split("-")[1]
        # Removing start from each cave's list helps a lot later
        if caveB!="start":
            try:    # if cave is already in dict
                cave_dict[caveA].append(caveB)
            except: # else create it in dict
                cave_dict[caveA] = [caveB]
        if caveA!="start":
            try:
                cave_dict[caveB].append(caveA)
            except:
                cave_dict[caveB] = [caveA]
    return cave_dict

# When in a cave, recursively enter its list of cave neighbours until end
def enterCave(here,cave_dict,visited_list,lowmax):
    path_count = 0
    # List number of times each small cave was visited
    lowercount_list = [visited_list.count(cave) for cave in visited_list if cave.islower()]
    for cave in cave_dict[here]:
        aux_list = visited_list.copy()
        # If neighbour is end, just increment the path count
        if cave=="end":
            path_count += 1
        # If neighbour is a big cave;
        #or if neighbour is a small cave but path didn't go through neither small cave <lowmax> times;
        #or if neighbour is a small cave and hasn't been visited yet
        elif cave.isupper() or not lowmax in lowercount_list or cave not in visited_list:
            aux_list.append(cave)
            path_count += enterCave(cave,cave_dict,aux_list,lowmax)
    return path_count

def part1(cave_dict,lowmax):
    return enterCave("start",cave_dict,["start"],lowmax)

# Read input file
cave_dict = file2list("../include/input12.inc")
print("----DAY 12----\nPart1: %s"%part1(cave_dict,1))
print("Part2: %s"%part1(cave_dict,2))