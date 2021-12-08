# Day 8 of the 2021 Advent of Code
class Entry():
    # Initiate the object
    def __init__(self,indata_list,outdata_list):
        self.pattern_list = indata_list
        self.digit_list = outdata_list

# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    entry_list = []
    for line in input_list:
        indata_list = (line.split(" | ")[0]).split(" ")
        outdata_list = (line.split(" | ")[1]).strip().split(" ")
        entry_list.append(Entry(indata_list,outdata_list))
    return entry_list

def part1(entry_list):
    # Only counts outputs that have a specific length
    unique_pattern_list = [2,4,3,7]
    unique_digit_count = 0
    for set in entry_list:
        for digit in set.digit_list:
            if len(digit) in unique_pattern_list : unique_digit_count += 1
    return unique_digit_count

def identifyDigits(pattern_list):
    seg_dict = {"top":"","mid":"","bot":"","upleft":"","downleft":"","upright":"","downright":""}
    num_list = [""]*10
    groupfive = []
    groupsix = []
    
    # Group numbers with known info
    for num in pattern_list:
        if len(num)==2: num_list[1] = num
        elif len(num)==3: num_list[7] = num
        elif len(num)==4: num_list[4] = num
        elif len(num)==5: groupfive.append(num)
        elif len(num)==6: groupsix.append(num)
        elif len(num)==7: num_list[8] = num
    
    # Find top
    topaux = num_list[7]
    for letter in num_list[1]:
        seg_dict["top"] = topaux.replace(letter,"")
        topaux = seg_dict["top"]
    
    # Find THREE
    for num in groupfive:
        for letter in num_list[1]:
            if letter not in num: break
        else: num_list[3] = num
    groupfive.remove(num_list[3])
    
    # Find SIX
    for num in groupsix:
        for letter in num_list[1]:
            if letter not in num:
                num_list[6] = num
                break
    groupsix.remove(num_list[6])

    # Find rightside
    for letter in num_list[1]:
        if letter in num_list[6]: seg_dict["downright"] = letter
        else: seg_dict["upright"] = letter
    
    # Find TWO and FIVE
    for num in groupfive:
        if seg_dict["upright"] in num: num_list[2] = num
        else: num_list[5] = num
    
    # Find leftside
    for letter in num_list[2]:
        if not(letter in num_list[5] or letter==seg_dict["upright"]):
            seg_dict["downleft"] = letter
            break
    for letter in num_list[5]:
        if not(letter in num_list[2] or letter==seg_dict["downright"]):
            seg_dict["upleft"] = letter
            break
    
    # Find ZERO and NINE
    for num in groupsix:
        if seg_dict["downleft"] in num: num_list[0] = num
        else: num_list[9] = num
    
    # Return list of patterns ordered
    return num_list

def part2(entry_list):
    outsum = 0
    for entry in entry_list:
        num_list = identifyDigits(entry.pattern_list)
        numdigits = 3
        # Adds up all numbers after matching each digit with a pattern
        for num in entry.digit_list:
            for i,each in enumerate(num_list):
                if "".join(sorted(num))=="".join(sorted(each)):
                    outsum += i*(10**numdigits)
                    numdigits -= 1
                    break
    return outsum

# Read input file
entry_list = file2list("../include/input8.inc")
print("----DAY 8----\nPart1: %s"%part1(entry_list))
print("Part2: %s"%part2(entry_list))