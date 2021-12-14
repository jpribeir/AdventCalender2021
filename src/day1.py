# Day 1 of the 2021 Advent of Code
# Count number of times a number is larger than the number x places before
# (A[n]+A[n-1]+A[n-2])-(A[n-1]+A[n-2]+A[n-3]) = A[n]+A[n-3]
def part2(sonar_list,x):
    return sum([1 for n in range(x,len(sonar_list)) if sonar_list[n]-sonar_list[n-x]>0])

# Read input file
with open("../include/input1.inc","r") as sonar_file:
    sonar_list = list(map(int,sonar_file.readlines()))

print("Part1: %s"%part2(sonar_list,1))
print("Part2: %s"%part2(sonar_list,3))