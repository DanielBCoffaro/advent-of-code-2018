
number = 0
num_list = [0]
found = False

filename = "data"
file = open(filename, "r")
lines = file.read().splitlines()
while not found:
    for line in lines:
        number = number + int(line)
        if number in num_list:
            print ("this one", number)
            found = True
            break
        else:
            num_list.append(number)
