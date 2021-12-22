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

def throwDie(jump_dict,old_position_dict,old_score_dict,finished_list):
    position_dict = {x:0 for x in range(1,11)}
    for pos in old_position_dict:
        for jump in jump_dict:
            position_dict[myModulo(pos+jump,10)] += old_position_dict[pos]*jump_dict[jump]
    # Each position should have its own score dictionary to keep track of what scores are in each position, that way you only have to add the die roll to that score and position pair
    score_dict = {pos: {x:0 for x in range(1,30)} for pos in range(1,11)}
    for pos in old_score_dict:
        for score in old_score_dict[pos]:
            for jump in jump_dict:
                score_dict[myModulo(pos+jump,10)][score+jump] += old_score_dict[pos][score]*jump_dict[jump]
    limited_score_dict = {pos: {x:score_dict[pos][x] for x in score_dict[pos] if x<=20} for pos in range(1,11)}
    finished_list.append(0)
    total_score_count = 0
    for pos in score_dict:
        for score in score_dict[pos]:
            if score>=21: finished_list[-1] += score_dict[pos][score]
            total_score_count += score_dict[pos][score]
    if total_score_count==0: return finished_list
    else: return throwDie(jump_dict,position_dict,limited_score_dict,finished_list)

def part2(start1,start2):
    jump_dict = {x:0 for x in range(3,10)}
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4): jump_dict[i+j+k] += 1
    position_dict = {x:1 if x==start1 else 0 for x in range(1,11)}
    score_dict = {pos: {x:0 for x in range(1,21)} for pos in range(1,11)}
    finished1_list = throwDie(jump_dict,position_dict,score_dict,[])
    print(finished1_list)
    #position_dict = {x:1 if x==start2 else 0 for x in range(1,11)}
    #score_dict = {pos: {x:0 for x in range(1,21)} for pos in range(1,11)}
    #finished2_list = throwDie(jump_dict,position_dict,score_dict,[])
    #print(finished2_list)

# Read input file
start1,start2 = file2list("../include/input21.inc")
print("----DAY 21----\nPart1: %s"%part1(start1,start2))
print("Part2: %s"%part2(4,8))