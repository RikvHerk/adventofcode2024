with open("day4.txt", "r") as file:
    data = file.readlines()

def check(data, i, j):
    c1 = data[i-1][j-1] == "M" and data[i+1][j+1] == "S"
    c2 = data[i-1][j-1] == "S" and data[i+1][j+1] == "M"
    c3 = data[i+1][j-1] == "M" and data[i-1][j+1] == "S"
    c4 = data[i+1][j-1] == "S" and data[i-1][j+1] == "M"
    
    if (c1 or c2) and (c3 or c4):
        return 1
    return 0

for i, line in enumerate(data):
    if i == len(data)-1:
        data[i] = list(line)
    else: 
        data[i] = list(line)[:-1]

result = 0
for i in range(len(data)-2):
    for j in range(len(data[i])-2):
        if data[i+1][j+1] == "A":
            result += check(data, i+1, j+1)

print(result)

