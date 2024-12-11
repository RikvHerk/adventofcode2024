with open("day4.txt", "r") as file:
    data = file.readlines()

def check(data, i, j, sign_i, sign_j):
    if i+3*sign_i >= 0 and j+3*sign_j >= 0:
        try:
            if data[i+sign_i][j+sign_j] == "M" and data[i+2*sign_i][j+2*sign_j] == "A" and data[i+3*sign_i][j+3*sign_j] == "S" :
                return 1
        except IndexError:
            return 0
    return 0

for i, line in enumerate(data):
    if i == len(data)-1:
        data[i] = list(line)
    else: 
        data[i] = list(line)[:-1]

result = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            for sign_i in range(3):
                for sign_j in range(3):
                    result += check(data, i, j, sign_i-1, sign_j-1)

print(result)

