filename = "C:/Users/Josh/Desktop/AdventOfCode/D1/input.txt"

dialLoc = 50
password = 0

with open(filename,'r') as file:
    for line in file:
        # print(line)
        if line[:1] == "R":
            for _ in range(int(line[1:])):
                dialLoc += 1
                if dialLoc == 100:
                    password += 1
                    dialLoc = 0
        else:
            for _ in range(int(line[1:])):
                dialLoc -= 1
                if dialLoc == 0:
                    password += 1
                elif dialLoc == -1:
                    dialLoc = 99
        # print(dialLoc)

print(password)
