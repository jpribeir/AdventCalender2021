# Day 3 of the 2021 Advent of Code
def file2list(input_filename,strip_en):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    if strip_en:
        cleaned_list = []
        for line in input_list:
            cleaned_list.append(line.strip())
        return cleaned_list
    else: return input_list

def part1(bin_list):
    listlen = len(bin_list)
    ones = [0] * len(bin_list[0])
    for num in bin_list:
        for i,bit in enumerate(num): ones[i] += int(bit)
    bin_gamma = ""
    bin_epsilon = ""
    for bit in ones:
        if bit < listlen/2:
            bin_gamma+="0"
            bin_epsilon+="1"
        else:
            bin_gamma+="1"
            bin_epsilon+="0"
    gamma = int(bin_gamma,2)
    epsilon = int(bin_epsilon,2)    
    return gamma*epsilon

def searchCode(bin_list,index,mcb):
    if len(bin_list) > 1:
        zeros_list = []
        ones_list = []
        for num in bin_list:
            if int(num[index]): ones_list.append(num)
            else: zeros_list.append(num)
        if mcb:
            if len(ones_list)==len(zeros_list): return searchCode(ones_list,index+1,mcb)
            else: return searchCode(max(ones_list,zeros_list,key=len),index+1,mcb)
        else:
            if len(ones_list)==len(zeros_list) or (not len(ones_list)): return searchCode(zeros_list,index+1,mcb)
            elif not len(zeros_list): return searchCode(ones_list,index+1,mcb)
            else: return searchCode(min(ones_list,zeros_list,key=len),index+1,mcb)
    elif len(bin_list) == 1: return bin_list[0]

def part2(bin_list):
    zeros_list = []
    ones_list = []
    for num in bin_list:
        if int(num[0]): ones_list.append(num)
        else: zeros_list.append(num)
        O2GR = searchCode(max(ones_list,zeros_list,key=len),1,True)
        CO2SR = searchCode(min(ones_list,zeros_list,key=len),1,False)
    return int(O2GR,2)*int(CO2SR,2)

# Read input file
bin_list = file2list("input3.inc",True)
print("Part1: %s"%part1(bin_list))
print("Part2: %s"%part2(bin_list))