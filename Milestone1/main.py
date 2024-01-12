import math

def readInputFile(file):
    with open(file, "r") as testcase:
        data = testcase.readlines()
        diameter = int(data[0].strip("WaferDiameter:"))
        n_points = int(data[1].strip("NumberOfPoints:"))
        angle = int(data[2].strip("Angle:"))
    return diameter, n_points, angle

def findPoints(diameter, n_points, angle):
    
    if angle not in [0, 180, 90, 270]:
        if 0 < angle < 90 or 180 < angle < 270:
            direction = "SW TO NE"
            if 180 < angle < 270:
                angle -= 180
        elif 90 < angle < 180 or 270 < angle < 360:
            direction = "NW TO SE"
            if 90 < angle < 180:
                angle = 180 - angle
            elif 270 < angle < 360:
                angle = 360 - angle
    points = []
    dist_bw_points = round(diameter / (n_points - 1), 4)
    radius = round(diameter/2, 4)
    
    if angle == 0 or angle == 180:
        point_start, point_end = [-radius, 0], [radius, 0]
        points.append(point_start)
        for i in range(n_points - 2):
            x = point_start[0] + (i+1)*dist_bw_points
            y = 0
            points.append([x, y])
        points.append(point_end)
    
    elif angle == 90 or angle == 270:
        point_start, point_end = [0, -radius], [0, radius]
        points.append(point_start)
        for i in range(n_points - 2):
            y = point_start[1] + (i+1)*dist_bw_points
            x = 0
            points.append([x, y])
        points.append(point_end)
    else:

        x_dist = (math.cos(math.radians(angle)) * dist_bw_points)
        y_dist = (math.sin(math.radians(angle)) * dist_bw_points)
        x_start, y_start = math.cos(math.radians(angle)) * radius, math.sin(math.radians(angle)) * (radius)

        if direction == "SW TO NE":
            point_start = [0-x_start, 0-y_start]
            points.append(point_start)
            for i in range(n_points - 2):
                x = point_start[0] + (i+1)*x_dist
                y = point_start[1] + (i+1)*y_dist
                points.append([x, y])
            point_end = [x_start, y_start]
            points.append(point_end)

        if direction == "NW TO SE":
            point_start = [0-x_start, y_start]
            points.append(point_start)
            for i in range(n_points - 2):
                x = point_start[0] + (i+1)*x_dist
                y = point_start[1] - (i+1)*y_dist
                points.append([x, y])
            point_end = [x_start, 0-y_start]
            points.append(point_end)
                
    return points
            
        
        

filenum = input("Enter test case number: ")
diameter, n_points, angle = readInputFile(f"D:\\21PC26_KLA_HACKATHON\\Milestone1\\Milestone1InputOutput\\Input\\Testcase{filenum}.txt")
points = findPoints(diameter, n_points, angle)

with open(f"Output{filenum}.txt", "w") as outfile:
    for i in range(len(points)):
        if i == len(points)-1:
            outfile.write(f"{tuple(points[i])}")
        else:            
            outfile.write(f"{tuple(points[i])}\n")
        
