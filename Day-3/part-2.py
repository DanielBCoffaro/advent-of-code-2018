from parse import parse
from collections import Counter

filename = "data"
file = open(filename, "r")

theray = []

for index, line in  enumerate(file):
    theray.append([])
    r = parse('#{id} @ {x},{y}: {xo}x{yo}', line)
    x = int(r['x'])+1
    y = int(r['y'])+1
    xo = int(r['xo'])
    yo = int(r['yo'])
    theray[index].append(r['id'])
    xray = list(range((x), (x+xo)))
    yray = list(range((y), (y+yo)))
    for i, x in enumerate(xray):
        for j, y in enumerate(yray):
            theray[index].append([x ,y])


def testpoints(box1, theray):
    for box2 in theray:
        if box1 != box2:
            for point in box1:
                if point in box2:
                    return
    print(box1[0])

for box1 in theray:
    testpoints(box1, theray)
