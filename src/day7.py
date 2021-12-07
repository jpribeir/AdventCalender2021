# Day 7 of the 2021 Advent of Code
####### List of all methods tried #######
import math
def allMethods(crab_list):
    # AVG #
    spot_avg = round(sum(crab_list)/len(crab_list))

    # MODE #
    mode_dict = {}
    for crab in crab_list:
        if crab in mode_dict: mode_dict[crab] += 1
        else: mode_dict[crab] = 1
    most_pop_spot = max(mode_dict,key=mode_dict.get)
    most_list = []
    for pos in mode_dict:
        if mode_dict[pos]==mode_dict[most_pop_spot]: most_list.append(pos)
    spot_mode = round(sum(most_list)/len(most_list))
    
    # MEAN #
    spot_mean = round((max(crab_list)+min(crab_list))/2)

    # MEDIAN #
    sort_list = [0]*(max(crab_list)+1)
    for crab in crab_list: sort_list[crab] += 1
    crab_count = 0
    i = 0
    while(crab_count<sum(sort_list)/2):
        crab_count += sort_list[i]
        spot_median = i
        i += 1
    
    # RMS #
    spot_rms = math.sqrt(sum(map(lambda x: x*x,crab_list))/len(crab_list))

    # GEOMETRIC MEAN #
    prod = 1
    for x in crab_list: prod *= x
    spot_geomean = prod*(1/len(crab_list))

    # SEARCH AROUND AVG #
    spending_dict = {}
    for spot in range(spot_avg-100,spot_avg+100):
        spending_dict[spot] = 0
        for index,crabs in enumerate(sort_list): spending_dict[spot] += finiteSum(spot-index)*crabs
    findval = min(spending_dict)
##################################

# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return list(map(int,input_file.read().split(",")))

def part1(crab_list):
    # Find the median
    crab_spot_list = [0]*(max(crab_list)+1)
    for crab in crab_list:
        crab_spot_list[crab] += 1
    crab_count = 0
    i = 0
    while(crab_count<sum(crab_spot_list)/2):    # Sum up all crabs found from first spot until half of the crabs
        crab_count += crab_spot_list[i]
        spot_median = i
        i += 1
    
    # Add up all used fuel
    fuel_spent = 0
    for crab in crab_list:
        fuel_spent += abs(crab-spot_median)
    return fuel_spent,crab_spot_list

# 1+2+3+...+n = n*(n+1)/2
def finiteSum(n):
    return int(abs(n)*(abs(n)+1)/2)

def part2(crab_list,crab_spot_list):
    # Find average spot and map all crabs in a list of spots
    spot_avg = round(sum(crab_list)/len(crab_list))
    
    # Create a dictionary of the possible spent fuel for a range of spots around the average spot
    spending_dict = {}
    for spot in range(spot_avg-100,spot_avg+100):
        spending_dict[spot] = 0
        for index,crabs in enumerate(crab_spot_list):
            spending_dict[spot] += finiteSum(spot-index)*crabs
    return spending_dict[min(spending_dict, key=spending_dict.get)]    # Return the spot with min fuel spent

# Read input file
crab_list = file2list("include/input7.inc")
result1,crab_spot_list = part1(crab_list)
print("----DAY 7----\nPart1: %s"%result1)
print("Part2: %s"%part2(crab_list,crab_spot_list))