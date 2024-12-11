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
i, j = si, sj
while nj >= 0 and ni >= 0:
    try:
        ni = i + direction[0]
        nj = j + direction[1]
        n[i, j] = 1
        if m[ni, nj] == ".":
            i = ni
            j = nj
        elif m[ni, nj] == "#":
            s = sum(direction)
            direction[0] += - direction[0] + direction[1]
            direction[1] -= s
    except IndexError:
        break

result = 0
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if n[i, j] == 1 and (i, j) != (si, sj):
            m1 = m.copy()
            m1[i, j] = "#"
            n1 = np.zeros(m1.shape)
            iters = 0
            nj, ni = 0, 0
            x, y = si, sj
            direction = np.array([-1, 0])
            while nj >= 0 and ni >= 0:
                iters += 1
                if iters > 2*np.sum(n1)+2:
                    result += 1
                    break
                try:
                    ni = x + direction[0]
                    nj = y + direction[1]
                    n1[x, y] = 1
                    if m1[ni, nj] == ".":
                        x = ni
                        y = nj
                    elif m1[ni, nj] == "#":
                        s = sum(direction)
                        direction[0] += - direction[0] + direction[1]
                        direction[1] -= s
                except IndexError:
                    break
print(result)
