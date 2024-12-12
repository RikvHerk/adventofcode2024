import numpy as np

with open("day9.txt", "r") as f:
    data = f.readlines()
    
data = [int(i) for i in list(data[0])]

m = []
x = 0
for i in np.arange(0, len(data)-1, 2):
    m += [x]*data[i]
    m += [-1]*data[i+1]
    x += 1

m += [x]*data[-1]

ind = 0
b = False
for i in np.arange(len(m)-1, 0, -1):
    if m[i] > -1 and not b:
        for j in np.arange(ind, len(m), 1):
            if j > i:
                b = True
                break
            if m[j] == -1:
                m[j] = m[i]
                m[i] = -1
                ind = j + 1
                break

result = 0
for i, j in enumerate(m):
    if j > -1:
        result += i*j

print(result)