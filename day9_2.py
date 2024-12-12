import numpy as np

with open("day9.txt", "r") as f:
    data = f.readlines()
    
data_n = [int(j) for i, j in enumerate(list(data[0])) if i%2 == 0]
data_gap = [int(j) for i, j in enumerate(list(data[0])) if i%2 == 1]

n = np.arange(len(data_n))

sorting = [[] for _ in range(len(data_gap))]

for i in np.arange(len(data_n)-1, 0, -1):
    for j in range(len(data_gap)):
        if j > i:
            break
        if data_n[i] <= data_gap[j]:
            sorting[j].append((n[i], data_n[i]))
            data_gap[j] -= data_n[i]
            n[i] = 0
            break
    
sequence = []
for i in range(len(data_gap)):
    sequence += [n[i]]*data_n[i]
    try:
        for m, l in sorting[i]:
            sequence += [m]*l
    except IndexError:
        pass
    sequence += [0]*data_gap[i]
sequence += [n[i]]*data_n[i]

result = 0.
for i, j in enumerate(sequence):
    result += i*j

print(result)