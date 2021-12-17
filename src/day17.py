# Day 16 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        line =  input_file.read().strip()
        x_line = (line.split(":")[1]).split(",")[0]
        y_line = (line.split(":")[1]).split(",")[1]
    


# Read input file
transmission = file2list("../include/input17.inc")

print("----DAY 16----\nPart1: %s"%result1)
#print("Part2: %s"%result2)