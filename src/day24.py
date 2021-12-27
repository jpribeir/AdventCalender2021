# Day 24 of the 2021 Advent of Code
"""
The whole code can be separated into 14 block of 18 lines, all follow the following pattern:
inp w
mul x 0
add x z
mod x 26
div z (A) -> Can be 1 or 26
add x (B) -> When A=1, it's something between 10 and 16; when A=26, it's a negative num
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (C) -> It's always a different num
mul y x
add z y

Simplified, each of the 14 block of 18 lines of code:
x = int((z%26 + B)!=w)
z //= A
z *= 25*x+1
z += (w+C)*x

When A=1 since B>9:
    x = 1 everytime;
    z //= A is dividing by 1 so it's a NOP
So it's essentially adding a digit in base 26 (multiplies the carryover by 26 and adds w+C):
z *= 26
z += (w+C)

Since half the blocks are A=1 and the other half is A=26, to make sure that in the end z=0,
each A=26 block (let's say beta) needs to subtract the digit the last A=1 block (alfa) added.
To ensure this happens, x=0 which means that w_alfa + C_alfa = w_beta - B_beta
This way each of the digits in the Model Number will be paired with another, and the w for the
most significant digit of the two is maximized in this equation, while both w_alfa and w_beta
stay within >0 and <9.
"""
class Digit():
    def __init__(self,a,i):
        self.index = i
        self.a = a
        self.b = 0
        self.c = 0
        self.digit = 0

# Convert input to a list
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return list(map(lambda x: x.strip(),input_file.readlines()))

def part1(instruction_list):
    # Stacks to store unpaired digits, lists store digits (index are the same for each pair)
    stackA,stackB,listA,listB = [],[],[],[]
    i = -1
    for line in instruction_list:
        if line.startswith("inp"):
            index = 0
            i += 1
        elif index==4: dig = Digit(int(line.split(" ")[2]),i)
        elif index==5: dig.b = int(line.split(" ")[2])
        elif index==15:
            dig.c = int(line.split(" ")[2])
            if dig.a==1:
                # If the opposing stack has content, store the last item and the new digit in respective lists
                if stackB:
                    listA.append(dig)
                    listB.append(stackB.pop(-1))
                # Else just stack the current digit until it finds a pair
                else: stackA.append(dig)
            else:
                if stackA:
                    listB.append(dig)
                    listA.append(stackA.pop(-1))
                else: stackB.append(dig)
        index += 1
    # Go through pairs, solve equation while maximizing the most significant digit
    for i,_ in enumerate(listA):
        wa = 9
        wb = wa + listA[i].c + listB[i].b
        while(wb<1 or wb>9):
            wa -= 1
            wb -= 1
        listA[i].digit = str(wa)
        listB[i].digit = str(wb)
    # Sort digits to return result
    bignum = ""
    for i in range(14):
        for j in listA+listB:
            if j.index==i:
                bignum += j.digit
                break
    # Go through pairs, solve equation while minimizing the most significant digit
    for i,_ in enumerate(listA):
        wa = 1
        wb = wa + listA[i].c + listB[i].b
        while(wb<1 or wb>9):
            wa += 1
            wb += 1
        listA[i].digit = str(wa)
        listB[i].digit = str(wb)
    # Sort digits to return result
    smallnum = ""
    for i in range(14):
        for j in listA+listB:
            if j.index==i:
                smallnum += j.digit
                break
    return bignum,smallnum

# Read input file
instruction_list = file2list("../include/input24.inc")
result1,result2 = part1(instruction_list)
print("----DAY 24----\nPart1: %s"%result1)
print("Part2: %s"%result2)