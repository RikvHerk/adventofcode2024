from itertools import product

def calc(seq, operations):
    x = int(seq[0])
    for i in range(len(operations)):
        if operations[i] == 0:
            x += int(seq[i+1])
        elif operations[i] == 1:
            x *= int(seq[i+1])
        elif operations[i] == 2:
            x = int(str(x) + seq[i+1])
    return x

with open("day7.txt", "r") as f:
    data = f.readlines()

data = [d.split(":") for d in data]

r = [int(i[0]) for i in data]
d = [i[1][1:].replace("\n", "").split(" ") for i in data]


result = 0
for i in range(len(d)):
    combs = product(*[[0, 1, 2]]*(len(d[i])-1))
    for c in combs:
        x = calc(d[i], c)
        if r[i] == x:
            result += r[i]
            break

print(result)

    