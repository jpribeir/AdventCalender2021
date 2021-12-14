# Day 4 of the 2021 Advent of Code
# Class fora each bingo puzzle
class Bingo():
    # Initiate the object
    def __init__(self):
        self.row_count = 5
        self.col_count = 5
        self.row_list = []
        self.row_score = [0]*self.row_count
        self.col_score = [0]*self.col_count
        self.total_sum = 0
        self.solved = False
    
    # Calculate sum of all elements in matrix
    def calcSum(self):
        for i in range(self.row_count):
            for j in range(self.col_count):
                self.total_sum += int(self.row_list[j][i])

# Convert input to a list, optional to strip \n
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    firstline_list = input_list[0].split(",")   # First line has list of bingo draws
    puzzle_list = []
    for line in input_list[1:]:
        if line.strip()=="":  # Emply lines come before the start of a puzzle
            puzzle_list.append(Bingo())
        else:                   # The remaining lines are part of a puzzle
            ((puzzle_list[-1]).row_list).append(line.strip().split())
    return firstline_list,puzzle_list

def searchPuzzle(puz,draw):
    for i,row in enumerate(puz.row_list):
        for j,item in enumerate(row):
            # If match is found corresponding row and column are marked, and element is subtracted from sum
            if item == draw:
                puz.row_score[i]+=1
                puz.col_score[j]+=1
                puz.total_sum -= int(draw)
                # If its row or column is completely marked this puzzle is solved and answer is returned
                if (puz.row_score[i] == puz.row_count) or (puz.col_score[i] == puz.col_count):
                    puz.solved = True       # In case 
                    return puz.total_sum*int(draw)
    return False

def part1(drawn_list,puzzle_list):
    for i,draw in enumerate(drawn_list):
        for puz in puzzle_list:
            answer = searchPuzzle(puz,draw)
            # If an answer is returned, return that answer and the draw list element wehre the search stopped
            if answer is not False:
                return answer,i

def part2(drawn_list,puzzle_list):
    num_unsolved = len(puzzle_list)-1   # Unsolved puzzles are all minus the one solved in part1
    for draw in drawn_list:
        for puz in puzzle_list:
            if puz.solved == False: # Only seach unsolved puzzles
                answer = searchPuzzle(puz,draw)
                # If an answer is returned, the total of unsolved puzzles is subtracted; when only one remains the answer is returned
                if answer is not False: num_unsolved -= 1
                if num_unsolved == 1: return answer

# Read input file
drawn_list,puzzle_list = file2list("../include/input4.inc")
for puz in puzzle_list: puz.calcSum()
result1,newstart = part1(drawn_list,puzzle_list)
print("Part1: %s"%result1)
print("Part2: %s"%part2(drawn_list[newstart:],puzzle_list))