# Day 2 of the 2021 Advent of Code
def part1(move_list):
    xx = 0
    zz = 0
    for move in move_list:
        direction = move.split()[0]
        value = int(move.split()[1])
        if direction == "forward": xx += value  # If forward, xx increases
        elif direction == "down": zz += value   # If down, zz increases
        elif direction == "up": zz -= value     # If up, zz decreases
    return xx*zz

def part2(move_list):
    xx = 0
    zz = 0
    aim = 0
    for move in move_list:
        direction = move.split()[0]
        value = int(move.split()[1])
        if direction == "forward":              # If forward,
            xx += value                         #   xx increases
            zz += (aim*value)                   #   zz increases multiplied by aim
        elif direction == "down": aim += value  # If down, aim increases
        elif direction == "up": aim -= value    # If up, aim decreases
    return xx*zz

# Read input file
move_list = []
with open("input2.inc","r") as move_file:
    move_list = move_file.readlines()

print("Part1: %s"%part1(move_list))
print("Part2: %s"%part2(move_list))