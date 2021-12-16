# Day 16 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return input_file.read().strip()

def getValueListed(val):
    return [val[0+i:5+i] for i in range(0,len(val),5)]

def hexaToBin(val_H):
    return bin(int(val_H, base=16))[2:].zfill(len(val_H)*4)

def versionControl(packet_B):
    if "1" not in packet_B: return 0
    version = packet_B[0:3]
    typeID = packet_B[3:6]
    value = packet_B[6:]
    # Type=4: value is a list of numbers
    if int(typeID,2)==4:
        val_list = getValueListed(value)
        for i,chunk in enumerate(val_list):
            value.pop(i)
            if chunk[0]: break
        return version + versionControl(value)
    # Type!=4: value is an operand
    else:
        # LengthID=0: next 15 bits are the length of bits to parse
        if value[0] == 0:
            values_length = int(value[1:17],2)
            return version + versionControl(value[17:17+values_length])   
        # LengthID=1: next 11 bits are the number of packets to parse
        else:
            values_count = int(value[1:13],2)
            ######### loop through count #########

def part1(tmsn_H):
    tmsn_B = hexaToBin(tmsn_H)
    return versionControl(tmsn_B)

# Read input file
transmission = file2list("../include/input16.inc")
example = "8A004A801A8002F478"
print("----DAY 16----\nPart1: %s"%part1(example))
#print("Part2: %s"%part2(extendMap(risk_map,5)))