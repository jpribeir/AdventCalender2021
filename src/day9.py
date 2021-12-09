# Day 9 of the 2021 Advent of Code
class Entry():
    # Initiate the object
    def __init__(self,indata_list,outdata_list):
        self.pattern_list = indata_list
        self.digit_list = outdata_list

# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    heat_map = []
    for line in input_list:
        heat_map.append(list(line.strip()))
    return heat_map

# This method doesn't prevent me from counting the same point multiple times
def part1(heat_map):
    map_width = len(heat_map[0])
    lowest_sum = 0
    for i,line in enumerate(heat_map):
        for j,point in enumerate(line):
            compare_list = []
            for m in range(-1,2):
                for n in range(-1,2):
                    try:
                        print("Comparing (%s,%s) with (%s,%s)"%(i,j,i+m,j+n))
                        compare_list.append(min(point,int(heat_map[i+m][j+n])))
                    except:
                        print("Scratch (%s,%s) with (%s,%s)"%(i,j,i+m,j+n))
                        pass
            lowest_sum += min(compare_list)
    return lowest_sum
# Read input file
heat_map = file2list("../include/input9.inc")
example_list = [[2,1,9,9,9,4,3,2,1,0,],
                [3,9,8,7,8,9,4,9,2,1],
                [9,8,5,6,7,8,9,8,9,2],
                [8,7,6,7,8,9,6,7,8,9],
                [9,8,9,9,9,6,5,6,7,8]]
print(example_list)
#print("----DAY 9----\nPart1: %s"%part1(entry_list))
print("----DAY 9----\nPart1: %s"%part1(example_list))
#print("Part2: %s"%part2(entry_list))