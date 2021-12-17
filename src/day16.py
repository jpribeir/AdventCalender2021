# Day 16 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return input_file.read().strip()

def getValueListed(val):
    return [val[0+i:5+i] for i in range(0,len(val),5)]

def decodePacket(packet_B):
    # Store this packet's version, typeID
    version = int(packet_B[0:3],2)
    typeID = int(packet_B[3:6],2)
    rest_of_packet = packet_B[6:]

    # Type=4: packet is a number
    if typeID==4:
        num_B = ""
        while rest_of_packet[0]!="0":
            num_B += rest_of_packet[1:5]
            rest_of_packet = rest_of_packet[5:]
        result = int(num_B+rest_of_packet[1:5],2)
        rest_of_packet = rest_of_packet[5:]

    # Type!=4: packet is an operation
    else:
        number_list = []
        # LengthID=0: next 15 bits are the length of bits to parse
        if rest_of_packet[0]=="0":
            values_length = int(rest_of_packet[1:16],2)
            rest_of_packet = rest_of_packet[16:]
            packet = rest_of_packet[:values_length]
            rest_of_packet = rest_of_packet[values_length:]
            while packet:
                sub_version,number,packet = decodePacket(packet)
                version += sub_version
                if number: number_list.append(number)
        
        # LengthID=1: next 11 bits are the number of packets to parse
        else:
            values_count = int(rest_of_packet[1:12],2)
            rest_of_packet = rest_of_packet[12:]
            for _ in range(values_count):
                sub_version,number,rest_of_packet = decodePacket(rest_of_packet)
                version += sub_version
                number_list.append(number)
        
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
    #### DEBUG PRINTS ####
    print("----------------------------------------------")
    print("typeID: %s"typeID)
    if typeID!=4:print(number_list)
    print("-> %s"%result)
    ######################
    return version,result,rest_of_packet

def part1(tmsn_H):
    return decodePacket(str(bin(int(tmsn_H,16))[2:].zfill(len(tmsn_H)*4)))

# Read input file
#transmission = file2list("../include/input16.inc")
transmission = file2list("../include/input_ricardo16.inc")
example1 = "C200B40A82"
example2 = "04005AC33890"
example3 = "880086C3E88112"
example4 = "CE00C43D881120"
example5 = "D8005AC2A8F0"
example6 = "F600BC2D8F"
example7 = "9C005AC2F8F0"
example8 = "9C0141080250320F1802104A08"
version,result2,_ = part1(transmission)
print("----DAY 16----\nPart1: %s"%version)
print("Part2: %s"%result2)