# Day 14 of the 2021 Advent of Code
# Convert input to a dict of lists
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    element_dict = {}
    pair_dict = {}
    initial_polymer = input_list[0].strip()
    for line in input_list[2:]:
        pair = line.split(" -> ")[0]
        newE = line.strip().split(" -> ")[1]
        pair_dict[pair] = newE
        if newE not in element_dict: element_dict[newE] = 0
    return initial_polymer,element_dict,pair_dict

# Recursively pairs the new element against the start and the end of the pair (for part2 would take ~infinite time)
def newElement(firstE,lastE,element_dict,pair_dict,time,maxtimes):
    newE = pair_dict[firstE+lastE]
    element_dict[newE] += 1
    time += 1
    # If still at less levels than max steps, enter recursion for 2 pairs
    if time<maxtimes:
        element_dict = newElement(firstE,newE,element_dict,pair_dict,time,maxtimes)
        element_dict = newElement(newE,lastE,element_dict,pair_dict,time,maxtimes)
    return element_dict

def part1(initial_polymer,element_dict,pair_dict,maxtimes):
    for element in initial_polymer: element_dict[element] += 1
    for i in range(1,len(initial_polymer)):
        element_dict = newElement(initial_polymer[i-1],initial_polymer[i],element_dict,pair_dict,0,maxtimes)
    # List count of all elements and return max()-min()
    count_list = [element_dict[e] for e in element_dict]
    return max(count_list) - min(count_list)

def part2(initial_polymer,element_dict,pair_dict,maxtimes):
    # Start by counting elements in initial polymer and prepare count dict for pairs
    for element in initial_polymer: element_dict[element] += 1
    count_dict = {pair:initial_polymer.count(pair) for pair in pair_dict}
    for time in range(maxtimes):
        new_counts = {pair:0 for pair in pair_dict}
        # Each pair this step will spawn 2 other pairs in the next
        for pair,counts in count_dict.items():
            element_dict[pair_dict[pair]] += counts
            new_counts[pair[0]+pair_dict[pair]] += counts
            new_counts[pair_dict[pair]+pair[1]] += counts
        count_dict = new_counts.copy()  # This ensures no pairs from the previous step carry over
    # List count of all elements and return max()-min()
    count_list = [element_dict[e] for e in element_dict]
    return max(count_list) - min(count_list)

# Read input file
initial_polymer,element_dict,pair_dict = file2list("../include/input14.inc")
print("----DAY 14----\nPart1: %s"%part1(initial_polymer,element_dict,pair_dict,10))
for e in element_dict: element_dict[e] = 0
print("Part2: %s"%part2(initial_polymer,element_dict,pair_dict,40))