# Day 1 of the 2021 Advent of Code
# Read input file
sonar_list = []
with open("input1.inc","r") as sonar_file:
    sonar_list = sonar_file.readlines()

# Count number of times a number is larger than its predecessor
inc_count = 0
for n in range(1,len(sonar_list)):
    if int(sonar_list[n])-int(sonar_list[n-1])>0: inc_count+=1
print(inc_count)

# Count number of times a number is larger than the number 3 places before
# (A[n]+A[n-1]+A[n-2])-(A[n-1]+A[n-2]+A[n-3]) = A[n]+A[n-3]
suminc_count = 0
for n in range(3,len(sonar_list)):
    if int(sonar_list[n])-int(sonar_list[n-3])>0: suminc_count+=1
print(suminc_count)