import numpy as np

with open("day8.txt", "r") as f:
    m = f.readlines()
    
m = np.array([list(line.replace("\n", "")) for line in m])

si, sj = m.shape

n = np.zeros((si,sj))

done = []

for i in range(si):
    for j in range(sj):
        if m[i, j] != ".":
            n[i, j] = 1
            if m[i, j] in done:
                continue
            done.append(m[i,j])
            pos = np.where(m==m[i,j])
            for p in range(len(pos[0])):
                for pp in range(len(pos[0])-1-p):
                    di = - pos[0][p] + pos[0][pp+p+1]
                    dj = - pos[1][p] + pos[1][pp+p+1]
                    
                    x = 1
                    while True:
                        
                        y = 0
                        ni = pos[0][p] - x*di
                        nj = pos[1][p] - x*dj
                        pi = pos[0][p] + (x+1)*di
                        pj = pos[1][p] + (x+1)*dj
                    
                        if 0 <= ni < si and 0 <= nj < sj:
                            n[ni, nj] = 1
                        else:
                            y += 1
                        if 0 <= pi < si and 0 <= pj < sj:
                            n[pi, pj] = 1
                        else:
                            y += 1
                        if y == 2:
                            break
                        else:
                            x += 1
                
print(np.sum(n))