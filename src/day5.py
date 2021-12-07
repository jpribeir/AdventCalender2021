# Day 5 of the 2021 Advent of Code
class Coord():
    # Initiate the object
    def __init__(self,xA,yA,xB,yB):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        if xA==xB or yA==yB:
            self.orthogonal = True
        else:
            self.orthogonal = False
    
    # Calculate sum of all elements in matrix
    def calcSum(self):
        for i in range(self.row_count):
            for j in range(self.col_count):
                self.total_sum += int(self.row_list[j][i])

# Convert input to a list
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        input_list = input_file.readlines()
    cleaned_list = []
    for line in input_list:
        cleaned_list.append(line.strip())
    return cleaned_list

# Create list of vents
def mapVents(coord_list):
    vent_list = []
    xmax = 0
    ymax = 0
    for coord in coord_list:
        cA = coord.split(" -> ")[0]
        xA = int(cA.split(",")[0])
        yA = int(cA.split(",")[1])
        cB = coord.split(" -> ")[1]
        xB = int(cB.split(",")[0])
        yB = int(cB.split(",")[1])
        vent_list.append(Coord(xA,yA,xB,yB))
        xmax = max(xmax,xA,xB)
        ymax = max(ymax,yA,yB)
    return vent_list,xmax,ymax

# If key exists increment, else set to 1
def fillEntry(fill_dict,newkey):
    if newkey not in fill_dict.keys():
        return 1
    else:
        return fill_dict[newkey]+1

# Count coordinates with 2 or more vents, return total
def countCoords(fill_dict):
    count_mults = 0
    for each in fill_dict:
        if fill_dict[each] > 1: count_mults += 1
    return count_mults

def part1(vent_list):
    fill_dict = {}
    for vent in vent_list:
        # Only look for horizontal and vertical
        if vent.orthogonal==True:
            # If vertical, fill line trough y values
            if vent.xA==vent.xB:
                start = min(vent.yA,vent.yB)
                end = max(vent.yA,vent.yB)
                for i in range(start,end+1):
                    newkey = str(vent.xA)+","+str(i)    # key is a string of coordinates
                    fill_dict[newkey] = fillEntry(fill_dict,newkey)
            # If horizontal, fill line trough x values
            else:
                start = min(vent.xA,vent.xB)
                end = max(vent.xA,vent.xB)
                for i in range(start,end+1):
                    newkey = str(i)+","+str(vent.yA)    # key is a string of coordinates
                    fill_dict[newkey] = fillEntry(fill_dict,newkey)
    
    # Return count, and fill_dict for part2
    return countCoords(fill_dict),fill_dict

def part2(vent_list,fill_dict):
    for vent in vent_list:
        # Only look for diagonal
        if vent.orthogonal==False:
            startx = min(vent.xA,vent.xB)
            endx = max(vent.xA,vent.xB)
            starty = min(vent.yA,vent.yB)
            
            # Line is filled with increasing x and increasing y
            if vent.xA-vent.xB==vent.yA-vent.yB:
                for i in range(endx-startx+1):
                    newkey = str(startx+i)+","+str(starty+i)
                    fill_dict[newkey] = fillEntry(fill_dict,newkey)
            # Line is filled with increasing x and decreasing y
            else:
                # Start with A if it has a smaller x
                if vent.xA<vent.xB: startx,starty = vent.xA,vent.yA
                # Start with B if it has a smaller x
                else:  startx,starty = vent.xB,vent.yB
                for i in range(endx-startx+1):
                    newkey = str(startx+i)+","+str(starty-i)
                    fill_dict[newkey] = fillEntry(fill_dict,newkey)
    
    # Count coordinates with 2 or more vents, return total
    return countCoords(fill_dict)

# Read input file
coord_list = file2list("include/input5.inc")
vent_list,xmax,ymax = mapVents(coord_list)
result1,fill_dict = part1(vent_list)
print("----DAY 5----\nPart1: %s"%result1)
print("Part2: %s"%part2(vent_list,fill_dict))