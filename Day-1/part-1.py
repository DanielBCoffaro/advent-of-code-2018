
number = 0
filename = "data"
file = open(filename, "r")
for line in file:
    number = number + int(line)

print(number)