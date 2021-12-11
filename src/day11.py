# Day 11 of the 2021 Advent of Code
# # Convert input to a list of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    octo_map = []
    for i,line in enumerate(input_list):
        auxlist = []
        for num in line.strip(): auxlist.append(int(num))
        octo_map.append(auxlist)
    return octo_map

# Updates each number it visits and its neighbours
def updateNum(octo_map,i,j,flash_count):
    # If index is in table's bounds
    if i in range(len(octo_map)) and j in range(len(octo_map[0])):
        octo_map[i][j] += 1
        # If an octopus just flashed update its neighbours and increment flashes
        if octo_map[i][j]==10:
            for m in range(-1,2):
                for n in range(-1,2):
                    if not (m==0 and n==0):
                        flash_count,octo_map = updateNum(octo_map,i+m,j+n,flash_count)
            flash_count += 1
    return flash_count,octo_map

# Updates the whole table for one step
def updateTable(octo_map,flash_count):
    for i,line in enumerate(octo_map):
            for j,num in enumerate(line):
                flash_count,octo_map = updateNum(octo_map,i,j,flash_count)
    # Revisit all octopuses that flashed and reset them to 0
    for i,line in enumerate(octo_map):
        for j,num in enumerate(line):
            if octo_map[i][j]>9: octo_map[i][j] = 0 
    return flash_count,octo_map

def part1(octo_map,numsteps):
    flash_count = 0
    step = 0
    while step<numsteps:
        flash_count,octo_map = updateTable(octo_map,flash_count)
        step += 1
    return flash_count,octo_map

def part2(octo_map,starting_steps):
    maxflash_count = len(octo_map)*len(octo_map[0])
    flash_count = 0
    step = starting_steps
    while(flash_count < maxflash_count):
        flash_count,octo_map = updateTable(octo_map,0)
        step += 1
    return step

# Read input file
octo_map = file2list("../include/input11.inc")
result1,out_map = part1(octo_map,100)
print("----DAY 11----\nPart1: %s"%result1)
print("Part2: %s"%part2(out_map,100))