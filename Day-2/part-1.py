from collections import Counter

filename = "data"
file = open(filename, "r")

counter2 = 0
counter3 = 0

for line in file:
    counts = Counter(line.strip())
    if 2 in counts.values():
        counter2 += 1
    if 3 in counts.values():
        counter3 += 1
print(counter2 * counter3)
