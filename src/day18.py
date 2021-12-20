# Day 18 of the 2021 Advent of Code
class Snail():
    # Initiate the object
    def __init__(self,depth,isPair):
        self.depth = depth
        self.isPair = isPair
        self.left = 0
        self.right= 0

# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return list(map(lambda x: x.strip(), input_file.readlines()))

def part1(function_list):
    pair_list = []
    for line in function_list:
        depth = 0
        pair_list.append(Snail(depth,True))
        for char in line:
            if char=="[":
                depth += 1
            elif char=="]":
                depth -= 1
            elif char==",":
                pass
            elif char.isdigit():
                if pass
            prevchar = char

# Read input file
function_list = file2list("../include/input18.inc")
example_list = file2list("../include/example18.inc")
print(example_list)
# [[[[8,8],[6,3]],[[0,2],[6,5]]],[[[7,6],[5,4]],[4,[7,1]]]]
# 1234...434...43234...434...4321234...434...4323..4...4321

print("----DAY 18----\nPart1: %s"%part1(example_list))
#print("Part2: %s"%result2)