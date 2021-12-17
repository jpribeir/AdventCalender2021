# Day 16 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return input_file.read().strip()

def getValueListed(val):
    return [val[0+i:5+i] for i in range(0,len(val),5)]

def hexaToBin(val_H):
    return str(bin(int(val_H,16))[2:].zfill(len(val_H)*4))

def versionControl(packet_B,ident):
    global print_en
    print_en = 0
    ident += ":"
    if print_en: print("------------------------------"*4)
    if print_en: print(packet_B)

    # If sending the zeros at the end of a value it can return 0
    if "1" not in packet_B: return False,""
    global result1
    result1 += int(packet_B[0:3],2)
    typeID = int(packet_B[3:6],2)
    value = packet_B[6:]
    if print_en: print("Version is %s ------- Total is %s"%(int(packet_B[0:3],2),result1))
    if print_en: print("Type is %s"%typeID)

    # Type=4: value is a list of numbers
    if typeID==4:
        val_list = getValueListed(value)
        number_B = ""
        for chunk in val_list.copy():
            number_B = number_B + val_list.pop(0)[1:]
            if chunk[0]=="0": break
        if print_en: print("Number is %s"%number_B)
        return int(number_B,2),"".join(val_list)

    # Type!=4: value is an operand
    else:
        number_list = []

        # LengthID=0: next 15 bits are the length of bits to parse
        if value[0] == "0":
            values_length = int(value[1:16],2)
            if print_en: print("%s -> Length is %s"%(value[0],values_length))
            packet = value[16:16+values_length]
            rest_of_packet = value[16+values_length:]
            if print_en: print("Packet is %s"%packet)
            if print_en: print("Rest is |%s|"%rest_of_packet)
            while packet:
                read_number,packet = versionControl(packet,ident)
                if read_number: number_list.append(read_number)
        
        # LengthID=1: next 11 bits are the number of packets to parse
        else:
            values_count = int(value[1:12],2)
            if print_en: print("%s -> Count is %s"%(value[0],values_count))
            packet = value[12:]
            if print_en: print("Rest is %s"%packet)
            for num in range(values_count):
                read_number,packet = versionControl(packet,ident)
                number_list.append(read_number)
            rest_of_packet = packet
        if print_en: print("Rest is %s"%rest_of_packet)
        
        # Choose operation
        if typeID==0: result = sum(number_list)
        elif typeID==1:
            result = 1
            for num in number_list: result *= num
        elif typeID==2: result = min(number_list)
        elif typeID==3: result = max(number_list)
        elif typeID==5: result = int(number_list[0]>number_list[1])
        elif typeID==6: result = int(number_list[0]<number_list[1])
        elif typeID==7: result = int(number_list[0]==number_list[1])
        if print_en: print("%s: type->%s"%(ident,typeID))
        if print_en: print("%s%s"%(ident,result))
        return result,rest_of_packet

def part1(tmsn_H):
    tsmn_B = hexaToBin(tmsn_H)
    return versionControl(tsmn_B,"")

# Read input file
transmission = file2list("../include/input16.inc")
result1 = 0
example = "C200B40A82"
example = "04005AC33890"
example = "880086C3E88112"
example = "CE00C43D881120"
example = "D8005AC2A8F0"
example = "F600BC2D8F"
example = "9C005AC2F8F0"
example = "9C0141080250320F1802104A08"
result2,no = part1(transmission)
print("----DAY 16----\nPart1: %s"%result1)
print("Part2: %s"%result2)