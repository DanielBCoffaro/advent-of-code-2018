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
    mindist = 1000
    for point in theray:
        mandist = (abs(point[0]-x))+(abs(point[1]-y))
        if mandist == mindist:
            smallestpoint = None
        if mandist < mindist:
            mindist = mandist
            smallestpoint = point
    return smallestpoint

def setsmalllist(x,y):
    smallestpoint = shortestdist(x,y)
    if smallestpoint and smallestpoint not in smallestpoints:
        smallestpoints.append(smallestpoint)

for x in range(maxX):
    setsmalllist(x,0)
    setsmalllist(x,maxY)

for y in range(maxY):
    setsmalllist(0,y)
    setsmalllist(maxX,y)

# print(smallestpoints)
# boundedlist = [x for x in theray if x not in smallestpoints]
# print (boundedlist)

points = []
for x in range(maxX):
    for y in range(maxY):
        curpoint = shortestdist(x,y)
        if curpoint:
            points.append(curpoint)


boundedlist = [x for x in points if x not in smallestpoints]
for i in range(len(boundedlist)):
    boundedlist[i] = str(boundedlist[i])
thecount = Counter(boundedlist)
print(thecount)