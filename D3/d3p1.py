filename = "C:/Users/Josh/Documents/AdventOfCode/adventofcode2025/D3/input.txt"

answer = 0

with open(filename,'r') as file:
    for line in file:
        largest = 0
        for i in range(len(line)):
            for j in range(i+1,len(line)):
                if int(line[i] + line[j]) > largest:
                    largest = int(line[i] + line[j])
        answer += largest
print(answer)
