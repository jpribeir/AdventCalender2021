# Day 6 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return list(map(int,input_file.read().split(",")))

########################
# First tried with recursion, couldn't get it to work
def countFamily(fish,starting_days):
    days_left = starting_days - fish - 1
    if days_left<=0: return 0
    child_count = int(days_left/7) + 1
    for child in range(child_count):
        child_count += countFamily(8,days_left-(child*7))
    return child_count
def oldPart1(fish_list):
    days_left = 80
    family_count = len(fish_list)
    for fish in fish_list: family_count += countFamily(fish,days_left)
    return family_count
########################

def part1(fish_rank,total_days):
    for day in range(total_days):
        birth = fish_rank[0]    # Fishes with 0 will give birth
        for i in range(8): fish_rank[i] = fish_rank[i+1]    # Every other fish goes down one number
        fish_rank[8] = birth    # Fishes in 8 are the newborns
        fish_rank[6] += birth   # Fishes in 6 are increased by the new fathers
    return sum(fish_rank)   # Return sum of whole list

# Read input file
fish_list = file2list("../include/input6.inc")
# Create list where each index contains the number of fishes with that number, and fill it
fish_rank = [0]*9
for i in fish_list: fish_rank[i] += 1
print("----DAY 6----\nPart1: %s"%part1(fish_rank,80))
print("Part2: %s"%part1(fish_rank,256))