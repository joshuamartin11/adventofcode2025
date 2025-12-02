filename = "C:/Users/Josh/Documents/AdventOfCode/adventofcode2025/D2/input.txt"

answer = 0

with open(filename,'r') as file:
    for line in file:
        for r in line.split(','):
            
            for x in range(int(r.split('-')[0]),int(r.split('-')[1]) + 1):
                string = str(x)
                middleIndex = len(string) // 2
                if string[:middleIndex] == string[middleIndex:]:
                    answer += x
print(answer)

