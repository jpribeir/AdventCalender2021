# Day 18 of the 2021 Advent of Code
class Snail():
    # Initiate the object
    def __init__(self,depth,risk,neighbour_list):
        self.depth = depth


# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        return list(map(lambda x: x.strip(), input_file.readlines()))

# Read input file
function_list = file2list("../include/input18.inc")
example_list = file2list("../include/example18.inc")
print(example_list)
# [[[[8,8],[6,3]],[[0,2],[6,5]]],[[[7,6],[5,4]],[4,[7,1]]]]
# 1234...434...43234...434...4321234...434...4323..4...4321

#print("----DAY 18----\nPart1: %s"%result1)
#print("Part2: %s"%result2)