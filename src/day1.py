# Day 1 of the 2021 Advent of Code
# Count number of times a number is larger than its predecessor
def part1(sonar_list):
    inc_count = 0
    for n in range(1,len(sonar_list)):
        if int(sonar_list[n])-int(sonar_list[n-1])>0: inc_count+=1
    return inc_count

# Count number of times a number is larger than the number 3 places before
# (A[n]+A[n-1]+A[n-2])-(A[n-1]+A[n-2]+A[n-3]) = A[n]+A[n-3]
def part2(sonar_list):
    suminc_count = 0
    for n in range(3,len(sonar_list)):
        if int(sonar_list[n])-int(sonar_list[n-3])>0: suminc_count+=1
    return suminc_count

# Read input file
sonar_list = []
with open("../include/input1.inc","r") as sonar_file:
    sonar_list = sonar_file.readlines()

print("Part1: %s"%part1(sonar_list))
print("Part2: %s"%part2(sonar_list))