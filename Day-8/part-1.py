from parse import parse
from collections import Counter

filename = "data"
file = open(filename, "r")

entries = file.read().split()

metadatannum = 0
index = 0

def additall(index):
    metanumber = entries[index+1]


    for i, x in enumerate(metanumber):
        metadatannum += entries[index+i]

additall(index)
print(metadatannum)
