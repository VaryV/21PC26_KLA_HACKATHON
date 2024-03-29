import sys
sys.setrecursionlimit(250000)


def readInputFile(file):
    with open(file, "r") as testcase:
        data = testcase.readlines()
        diameter = int(data[0].strip("WaferDiameter:"))
        die_size = [int(data[1].strip("DieSize:").split("x")[0]), int(data[1].strip("DieSize:").split("x")[1])]
        DieShiftVector = data[2].strip("DieShiftVector:")
        ReferenceDie = data[3].strip("ReferenceDie:")
        DieShiftVector = [DieShiftVector.split(",")[0].strip("("), DieShiftVector.split(",")[1].strip(")\n")]
        dieShift = [int(DieShiftVector[0]), int(DieShiftVector[1])]
        ReferenceDie = [ReferenceDie.split(",")[0].strip("("), ReferenceDie.split(",")[1].strip(")\n")]
        refDie = [int(ReferenceDie[0]), int(ReferenceDie[1])]
        
        
    return diameter, die_size, dieShift, refDie


def LLCinWafer(point):
    x, y = point
    if x**2 + y**2 < radius ** 2:
        return True#x**2 + y**2
    return False


def dfs(x, y, coordinates):
    x_c , y_c = coordinates[0], coordinates[1]
    res = (LLCinWafer(coordinates) or LLCinWafer((x_c+size_x, y_c)) or LLCinWafer((x_c, y_c+size_y)) or LLCinWafer((x_c+size_x, y_c+size_y)))
    if (x, y) not in d and res:
        print(x, y, coordinates)
        d[(x, y)] = coordinates
        dfs(x+1, y, (coordinates[0] + size_x, coordinates[1]))
        dfs(x-1, y, (coordinates[0] - size_x, coordinates[1]))
        dfs(x, y+1, (coordinates[0], coordinates[1] + size_y))
        dfs(x, y-1, (coordinates[0], coordinates[1] - size_y))
        return
    else:
        print("Done with this direction")
        return        

# def bfs():
#     queue = []
#     co_queue = []
#     queue.append((0, 0))
#     co_queue.append((ReferenceDie[0]-(size_x/2), ReferenceDie[1]-(size_y/2)))
#     directions = [[1,0], [-1,0], [0, 1], [0, -1]]
#     while queue:
#         c, c_co = queue.pop(0), co_queue.pop()
#         res = (LLCinWafer(c_co) or LLCinWafer((c_co[0]+size_x, c_co[1])) or LLCinWafer((c_co[0], c_co[1]+size_y)) or LLCinWafer((c_co[0]+size_x, c_co[1]+size_y)))
#         if c not in d and res:
#             d[c] = c_co
#         for i in directions:
#             queue.append((c[0]+i[0], c[1]+i[1]))
#             co_queue.append((c_co[0]+i[0]*size_x, c_co[1]+i[1]*size_y))
    
            
filenum = input("Enter test case number: ")
diameter, die_size, DieShiftVector, ReferenceDie = readInputFile(f"D:\\21PC26_KLA_HACKATHON\\Milestone2\\Milestone2InputOutput\\Input\\Testcase{filenum}.txt")
radius = diameter / 2
size_x, size_y = die_size[0], die_size[1]
center = (0, 0)
d = {}
print((ReferenceDie[0]-(size_x/2), ReferenceDie[1]-(size_y/2)))
# dfs(0, 0, (ReferenceDie[0]-(size_x/2), ReferenceDie[1]-(size_y/2)))
# bfs()
print(len(d))

with open(f"D:\\21PC26_KLA_HACKATHON\\Milestone2\\Output{filenum}.txt", "w") as outfile:
    for i in d:
        outfile.write(f"{i}:{d[i]}\n")