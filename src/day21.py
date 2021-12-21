# Day 21 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        lines =  input_file.readlines()
    return int(lines[0].split(": ")[1].strip()),int(lines[1].split(": ")[1].strip())

def myModulo(num,base):
    if num%base==0: return base
    else: return num%base

def part1(start1,start2):
    position_list = [start1,start2]
    score_list = [0,0]
    roll = 0
    total_count = 0
    while True:
        for i,_ in enumerate(position_list):
            jump = 0
            for _ in range(3):
                roll = myModulo(roll+1,100)
                jump += roll
                total_count += 1
            position_list[i] = myModulo(position_list[i]+jump,10)
            score_list[i] += position_list[i]
            if score_list[i]>=1000: return total_count*min(score_list)

def throwDie(player1,player2):
    pass
    #throwDie(player2,player1)

def part2(start1,start2):
    jump_dict = {x:0 for x in range(3,10)}
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4): jump_dict[i+j+k] += 1
    position_dict = {x:0 for x in range(1,11)}
    position_dict[start1] = 1
    old_dict = position_dict.copy()
    position_dict = {x:0 for x in range(1,11)}
    for pos in old_dict:
        if old_dict[pos]!=0:
            print("Position: %s"%pos)
            for jump in jump_dict:
                print(myModulo(jump+pos,10))
                position_dict[myModulo(pos+jump,10)] = old_dict[pos]*jump_dict[jump]
    for line in old_dict: print("%s: %s"%(line,old_dict[line]))
    for line in position_dict: print("%s: %s"%(line,position_dict[line]))
    throwDie(start1,start2)

# Read input file
start1,start2 = file2list("../include/input21.inc")
print("----DAY 21----\nPart1: %s"%part1(start1,start2))
print("Part2: %s"%part2(4,8))