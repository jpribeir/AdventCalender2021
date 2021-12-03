# Day 3 of the 2021 Advent of Code
# Convert input to a list, optional to strip \n
def file2list(input_filename,strip_en):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    if strip_en:
        cleaned_list = []
        for line in input_list:
            cleaned_list.append(line.strip())
        return cleaned_list
    else: return input_list

def searchCode(bin_list,index,mcb):
    if len(bin_list) > 1:
        zeros_list = []
        ones_list = []
        for num in bin_list:
            if int(num[index]): ones_list.append(num)   # list of 1s in current index
            else: zeros_list.append(num)                # list of 0s in current index
        if mcb: # if searching for the most common occurence
            if len(ones_list)==len(zeros_list): return searchCode(ones_list,index+1,mcb)    # if lists are the same size, return 1s
            else: return searchCode(max(ones_list,zeros_list,key=len),index+1,mcb)          # else return the longest
        else:   # if searching for the least common occurence
            if len(ones_list)==len(zeros_list) or (not len(ones_list)): return searchCode(zeros_list,index+1,mcb)   # if lists are the same size or only 0s occur, return 0s
            elif not len(zeros_list): return searchCode(ones_list,index+1,mcb)      # if no zeros occur, return 1s
            else: return searchCode(min(ones_list,zeros_list,key=len),index+1,mcb)  # else return the shortest
    elif len(bin_list) == 1: return bin_list[0] # if only 1 number, return it

def part1(bin_list):
    ones = [0] * len(bin_list[0])
    for num in bin_list:
        for i,bit in enumerate(num): ones[i] += int(bit)    # count number of times 1 is found in each index
    bin_gamma = ""
    bin_epsilon = ""
    for bit in ones:
        if bit > len(bin_list)/2:   # if 1 has more occurences, add 1 to gamma and 0 to epsilon
            bin_gamma+="1"
            bin_epsilon+="0"
        else:                       # otherwise...
            bin_gamma+="0"
            bin_epsilon+="1"

    # convert to decimal
    gamma = int(bin_gamma,2)
    epsilon = int(bin_epsilon,2)    
    return gamma*epsilon

def part2(bin_list):
    zeros_list = []
    ones_list = []
    for num in bin_list:
        if int(num[0]): ones_list.append(num)   # list of 1s in index 0
        else: zeros_list.append(num)            # list of 0s in index 0
        O2GR = searchCode(max(ones_list,zeros_list,key=len),1,True)     # search for the code with the most occuring bit in each index
        CO2SR = searchCode(min(ones_list,zeros_list,key=len),1,False)   # search for the code with the least occuring bit in each index
    return int(O2GR,2)*int(CO2SR,2)

# Read input file
bin_list = file2list("input3.inc",True)
print("Part1: %s"%part1(bin_list))
print("Part2: %s"%part2(bin_list))