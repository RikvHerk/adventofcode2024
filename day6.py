import numpy as np

with open("day6.txt", "r") as f:
    m = f.readlines()
    
m = np.array([list(line.replace("\n", "")) for line in m])
n = np.zeros(m.shape)

si, sj = np.where(m == "^")
si = si[0]
sj = sj[0]

m[si, sj] = "."


direction = np.array([-1, 0])

nj, ni = 0, 0 
while nj >= 0 and ni >= 0:
    try:
        ni = si + direction[0]
        nj = sj + direction[1]
        n[si, sj] = 1
        if m[ni, nj] == ".":
            si = ni
            sj = nj
        elif m[ni, nj] == "#":
            s = sum(direction)
            direction[0] += - direction[0] + direction[1]
            direction[1] -= s
    except IndexError:
        break
    
print(np.sum(n))