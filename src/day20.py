# Day 20 of the 2021 Advent of Code
# Convert input to a matrix
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        algorithm = input_file.readline()
        pixel_map = list(map(lambda x: x.strip(),input_file.readlines()[1:]))
    return algorithm,pixel_map

def part1(algorithm,pixel_map):
    pass

# Read input file
algorithm,pixel_map = file2list("../include/input20.inc")
example_algorithm,example_map = file2list("../include/example20.inc")
print("----DAY 20----\nPart1: %s"%part1(example_algorithm,example_map))
#print("Part2: %s"%part1(instruction_list,maxval))