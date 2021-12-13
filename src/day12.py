# Day 12 of the 2021 Advent of Code
# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    cave_dict = {}
    for line in input_list:
        caveA = line.strip().split("-")[0]
        caveB = line.strip().split("-")[1]
        if caveB!="start":
            try:
                cave_dict[caveA].append(caveB)
            except:
                cave_dict[caveA] = [caveB]
        if caveA!="start":
            try:
                cave_dict[caveB].append(caveA)
            except:
                cave_dict[caveB] = [caveA]
        
    return cave_dict

def enterCavePart1(here,cave_dict,visited_list,ident):
    print("%s%s"%(ident,visited_list))
    path_count = 0
    for cave in cave_dict[here]:
        aux_list = visited_list.copy()
        if cave.isupper():
            aux_list.append(cave)
            path_count += enterCavePart1(cave,cave_dict,aux_list,ident+":")
        elif cave=="end":
            visited_list.append(cave)
            print("%s%s<---"%(ident,visited_list))
            path_count += 1
        elif cave not in visited_list:
            aux_list.append(cave)
            path_count += enterCavePart1(cave,cave_dict,aux_list,ident+":")
    print("%s%s paths found on this level"%(ident,path_count))
    return path_count

def enterCave(here,cave_dict,visited_list,ident,lowmax):
    #print("%s%s"%(ident,visited_list))
    path_count = 0
    lower_dict = {cave:visited_list.count(cave) for cave in cave_dict[here] if cave.islower()}
    for cave in cave_dict[here]:
        aux_list = visited_list.copy()
        print("%s%s"%(ident,lower_dict))
        if cave.isupper():
            aux_list.append(cave)
            path_count += enterCave(cave,cave_dict,aux_list,ident+":",lowmax)
        elif cave=="end":
            visited_list.append(cave)
            print("%s%s<---"%(ident,visited_list))
            #print("%sReached end at %s!"%(ident,here))
            path_count += 1
        elif not lowmax in lower_dict.values():
            aux_list.append(cave)
            path_count += enterCave(cave,cave_dict,aux_list,ident+":",lowmax)
        elif cave not in visited_list:
            aux_list.append(cave)
            path_count += enterCave(cave,cave_dict,aux_list,ident+":",lowmax)
    #print("%s%s paths found on this level"%(ident,path_count))
    return path_count

def part1(cave_dict):
    return enterCavePart1("start",cave_dict,["start"],"")

def part2(cave_dict):
    return enterCave("start",cave_dict,["start"],"",2)

# Read input file
cave_dict = file2list("../include/input12.inc")
example_dict = file2list("../include/example12.inc")
#print(example_dict)
#print("----DAY 12----\nPart1: %s"%part1(example_dict))
print("Part2: %s"%part2(example_dict))