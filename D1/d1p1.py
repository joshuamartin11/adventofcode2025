filename = "C:/Users/Josh/Documents/AdventOfCode/adventofcode2025/D1/input.txt"

dialLoc = 50
password = 0

with open(filename,'r') as file:
    for line in file:
        # print(line)
        if line[:1] == "R":
            dialLoc += int(line[1:])
        else:
            dialLoc -= int(line[1:])
        dialLoc = dialLoc % 100
        if dialLoc == 0:
            password += 1
        # print(dialLoc)

print(password)

