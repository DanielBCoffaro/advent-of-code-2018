
def findit():
    filename = "data"
    file = open(filename, "r")
    lines = file.read().splitlines()

    for line in lines:
        for lineC in lines:
            diffCounter = 0
            if line != lineC:
                for index in range(len(line)):
                    if line[index] != lineC[index]:
                        diffCounter += 1
                    if diffCounter >= 2:
                        break
                if diffCounter == 1:
                    print(line)
                    print(lineC)
                    return

findit()
