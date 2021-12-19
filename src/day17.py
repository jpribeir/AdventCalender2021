# Day 17 of the 2021 Advent of Code
# Convert input to a string
def file2list(input_filename):
    with open(input_filename,"r") as input_file:
        line =  input_file.read().strip()
    x_line = (line.split(":")[1]).split(",")[0]
    y_line = (line.split(":")[1]).split(",")[1]
    xA,xB = x_line.split("=")[1].split("..")
    yA,yB = y_line.split("=")[1].split("..")
    return range(int(xA),int(xB)+1),range(int(yA),int(yB)+1)

def part1(xrange,yrange):
    ymax_list = []
    start_count = 0
    # Loop trough the minimum and maximum velocities that reach the area limits
    for xvel in range(xrange[0]//10,xrange[-1]+1):
        for yvel in range(-abs(yrange[0]),abs(yrange[0])):
            reachable = True
            ymax = 0
            x,y = 0,0
            vx,vy = xvel,yvel
            while reachable:
                # Update position according to velocity, and update maximum y
                x += vx
                y += vy
                ymax = max(ymax,y)
                # Update velocities according to drag and gravity
                if vx!=0: vx += -(vx//abs(vx))
                vy -= 1
                # If position inside area
                if x in xrange and y in yrange:
                    reachable = False
                    ymax_list.append(ymax)
                    start_count += 1
                # Else if passed max x or max y
                elif x>xrange[-1] or y<yrange[0]: reachable = False
    return max(ymax_list), start_count

# Read input file
xrange,yrange = file2list("../include/input17.inc")
result1,result2 = part1(xrange,yrange)
print("----DAY 17----\nPart1: %s"%result1)
print("Part2: %s"%result2)