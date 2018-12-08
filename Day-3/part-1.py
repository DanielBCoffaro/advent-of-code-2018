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
    xray = list(range((x), (x+xo)))
    yray = list(range((y), (y+yo)))
    for i, x in enumerate(xray):
        for j, y in enumerate(yray):
            theray[index].append([x,y])

newray = []
for i, box in enumerate(theray):
    newray = newray + box
newray = map(tuple, newray)
thecount = Counter(newray)
its = list(thecount.values())
count = 0
for i, j in enumerate(its):
    if j > 1:
        count += 1
print(count)