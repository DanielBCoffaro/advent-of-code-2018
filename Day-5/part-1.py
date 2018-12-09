from parse import parse
from collections import Counter

filename = "data"
file = open(filename, "r")
input = file.read()

found_something = True

while found_something:
    i = 0
    found_something = False
    while i < len(input)-1:
        if input[i].lower() == input[i+1].lower():
            if input[i].isupper():
                if input[i+1].islower():
                    input = input[:i] + input[i+2:]
                    found_something = True
            elif input[i].islower():
                if input[i+1].isupper():
                    input = input[:i] + input[i+2:]
                    found_something = True
        i += 1

print(len(input))