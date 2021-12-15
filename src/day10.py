# Day 10 of the 2021 Advent of Code
global matching_dict
matching_dict = {"(":")","[":"]","{":"}","<":">"}

# Convert input to a list os strings
def file2list(input_filename):
	with open(input_filename,"r") as input_file:
		return list(map(lambda a: a.strip(),input_file.readlines()))

# Recursion (yey)
def enterNest(index,chunk_line):
	while(True):
		# If this is the final character in the list, end
		if index >= len(chunk_line): return "end"
		# If opening a nest, go next
		if chunk_line[index] in matching_dict.keys():
			pivot = enterNest(index+1,chunk_line)
			try:	# If return is an int
				pivot = int(pivot)
				# If returned character matches this recursion's character
				if chunk_line[pivot] == matching_dict[chunk_line[index]]: index = pivot + 1
				# Else an error was found
				else: return chunk_line[pivot]
			except:	# Else the error was found in the recursion
				return pivot
		# Else it's closing a nest
		else: return index

def part1(chunk_list):
	points_dict = {")":3,"]":57,"}":1197,">":25137}
	score = 0
	healthy_list = []
	for line in chunk_list:
		# Start recursion at first chunk in line
		result = enterNest(0,line)
		# If end, a broken line was found, add up result to score
		if result is not "end": score += points_dict[result]
		# Else it's a healthy line
		else: healthy_list.append(line)
	return score,healthy_list

def part2(chunk_list):
	points_dict = {")":1,"]":2,"}":3,">":4}
	score_list = [0]*len(chunk_list)
	for i,line in enumerate(chunk_list):
		openings = ""
		for chunk in line:
			# If closing chunk, remove last corresponding opening chunk
			if chunk in points_dict:
				deleted = list(matching_dict.keys())[list(matching_dict.values()).index(chunk)]
				openings = openings.replace(deleted,"",1)
			# Else add opening chunk to the reversed list
			else: openings = chunk+openings
		# Calculate score
		for char in openings:
			score_list[i] *= 5
			score_list[i] += points_dict[matching_dict[char]]
	score_list.sort()
	return score_list[int((len(score_list)-1)/2)]

# Read input file
chunk_list = file2list("../include/input10.inc")
result1,healthy_list = part1(chunk_list)
print("----DAY 10---\nPart1: %s"%result1)
print("Part2: %s"%part2(healthy_list))
