from parse import parse
from collections import Counter

filename = "data"
file = open(filename, "r")

theray = []
maxX=0
maxY=0

for index, line in enumerate(file):
    r = parse('{x}, {y}', line)
    theray.append([int(r['x']), int(r['y'])])
    if theray[index][0] > maxX:
        maxX = theray[index][0]
    if theray[index][1] > maxY:
        maxY = theray[index][1]

maxX =maxX + 1
maxY =maxY + 1
testray = theray
smallestpoints = []

def shortestdist(x,y):
    sumofdist = 0
    for point in theray:
        mandist = (abs(point[0]-x))+(abs(point[1]-y))
        sumofdist = sumofdist + mandist
    return sumofdist < 10000

total = 0

for x in range(maxX):
    for y in range(maxY):
        if shortestdist(x,y):
            total += 1

print(total)