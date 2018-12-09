from parse import parse
from string import ascii_lowercase
from string import ascii_uppercase

filename = "data"
file = open(filename, "r")
input = file.read()

def reactit(input):
    found_something = True

    while found_something:
        i=0
        found_something = False
        while i < len(input)-1:
            if input[i].lower() == input[i+1].lower():
                if input[i].isupper():
                    if input[i+1].islower():
                        input = input[:i] + input[i+2:]
                        found_something = True
                        i-=1
                elif input[i].islower():
                    if input[i+1].isupper():
                        input = input[:i] + input[i+2:]
                        found_something = True
                        i-=1
            i += 1
    return input

shortestinput = input
for l in ascii_lowercase:
    newinput = input.replace(l, "")
    newinput = newinput.replace(l.upper(), "")
    newinput = reactit(newinput)
    if (len(newinput)) < len(shortestinput):
        shortestinput = newinput

print(len(shortestinput))
