# Day 13 of the 2021 Advent of Code
# Convert input to a matrix
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    instruction_list = []
    dot_list = []
    xmax = 0
    ymax = 0
    for line in input_list:
        if line.startswith("fold"):
            instruction_list.append(line.strip().split(" ")[2])
        elif "," in line:
            x,y = int(line.split(",")[0]),int(line.split(",")[1])
            xmax = max(xmax,x)
            ymax = max(ymax,y)
            dot_list.append([x,y])
    # For some reason it needs to check if input creates a matrix with odd number rows...
    if ymax%2!=0: ymax += 1
    dot_map = [[" " for i in range(xmax+1)] for j in range(ymax+1)]
    for line in dot_list: dot_map[line[1]][line[0]] = "█"
    return dot_map,instruction_list

# Transpose matrix
def transposeMap(dot_map):
    zipped_rows = zip(*dot_map)
    transposed = [list(row) for row in zipped_rows]
    return transposed

# Folds map according to single instruction
def foldMap(dot_map,instruction):
    # If horizontal fold, transpose matrix
    if instruction.split("=")[0]=="x": dot_map = transposeMap(dot_map)
    fold = int(instruction.split("=")[1])
    first_half = dot_map[0:fold]    # from start to fold index
    second_half = list(reversed(dot_map[fold+1:]))  # from fold index to end
    for i,line in enumerate(second_half):
        for j,col in enumerate(line):
            # If any of the two is a marked space, mark the space
            if first_half[i][j]=="█" or second_half[i][j]=="█": first_half[i][j] = "█"
            else: first_half[i][j] = " "
    if instruction.split("=")[0]=="x": first_half = transposeMap(first_half)
    return first_half

# Prints a row at a time
def printMap(dot_map):
    for line in dot_map:
        outstr = ""
        for char in line: outstr += char
        print(outstr)
    print("\n")

def part1(dot_map,instruction):
    folded_map = foldMap(dot_map,instruction)
    dot_count = 0
    for line in folded_map: dot_count += line.count("█")
    return dot_count

def part2(dot_map,instruction_list):
    tofold_map = dot_map
    for each in instruction_list: tofold_map = foldMap(tofold_map,each)
    printMap(tofold_map)

# Read input file
dot_map,instruction_list = file2list("../include/input13.inc")
print("----DAY 13----\nPart1: %s"%part1(dot_map,instruction_list[0]))
print("\nPart2:")
part2(dot_map,instruction_list)