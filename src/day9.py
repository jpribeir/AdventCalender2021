# Day 9 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
	with open(input_filename,"r") as input_file:
		input_list = input_file.readlines()
	heat_map = []
	for line in input_list:
		heat_map.append(list(line.strip()))
	return heat_map

# Returns a unique ID based on matrix coordinates
def getID(i,j):
	return i*MAPW + j

# Recursively checks a point's neighbours for a lower point
def checkNeighbours(i,j,heat_map,lows_list,checked_list):
	checked_list.append(getID(i,j))
	for n in [-1,1]:
		# If it's a valid index, and if new point is lower
		if (j+n) in range(MAPW) and int(heat_map[i][j+n]) <= int(heat_map[i][j]):
				if getID(i,j+n) in checked_list: return lows_list,checked_list
				else: return checkNeighbours(i,j+n,heat_map,lows_list,checked_list)
	for n in [-1,1]:
		if (i+n) in range(MAPH) and int(heat_map[i+n][j]) <= int(heat_map[i][j]):
				if getID(i+n,j) in checked_list: return lows_list,checked_list
				else: return checkNeighbours(i+n,j,heat_map,lows_list,checked_list)
	
	# Finishing both loops means this is a low point!
	else:
		lows_list.append(getID(i,j))
		for n in [-1,1]:
			# If it's a valid index, and if point hasn't been checked
			if (j+n) in range(MAPW) and getID(i,j+n) not in checked_list:
				checked_list.append(getID(i,j+n))
		for n in [-1,1]:
			if (i+n) in range(MAPH) and getID(i+n,j) not in checked_list:
				checked_list.append(getID(i+n,j))
		return lows_list,checked_list

def part1(heat_map):
	checked_list = []
	lows_list = []
	for i,line in enumerate(heat_map):
		for j,point in enumerate(line):
			if getID(i,j) not in checked_list:
				lows_list,checked_list = checkNeighbours(i,j,heat_map,lows_list,checked_list)
	
	# Add up all low points found
	lows_sum = 0
	for id in lows_list:
		row = int(id/MAPW)
		col = id - row*MAPW
		lows_sum += (1 + int(heat_map[row][col]))
	return lows_sum,lows_list

# Recursively measures a low point's basin
def mapBasin(i,j,heat_map,mapped_list):
	mapped_list.append(getID(i,j))
	for n in [-1,1]:
		# If it's a valid index, if point hasn't been mapped, and if it's lower than 9
		if ((j+n) in range(MAPW) and getID(i,j+n) not in mapped_list) and int(heat_map[i][j+n]) < 9:
			mapped_list = mapBasin(i,j+n,heat_map,mapped_list)
	for n in [-1,1]:
		if ((i+n) in range(MAPH) and getID(i+n,j) not in mapped_list) and int(heat_map[i+n][j]) < 9:
			mapped_list = mapBasin(i+n,j,heat_map,mapped_list)
	return mapped_list

def part2(heat_map,lows_list):
	basin_list = []
	for id in lows_list:
		i = int(id/MAPW)
		j = id - i*MAPW
		basin_list.append(len(mapBasin(i,j,heat_map,[])))
	
	# Multiply 3 biggest basins' sizes
	size_prod = 1
	basin_list.sort()
	for rank in range(3): size_prod *= basin_list.pop()
	return size_prod

# Read input file
heat_map = file2list("../include/input9.inc")
global MAPW
global MAPH
MAPW = len(heat_map[0])
MAPH = len(heat_map)
result1,lows_list = part1(heat_map)
print("----DAY 9----\nPart1: %s"%result1)
print("Part2: %s"%part2(heat_map,lows_list))
