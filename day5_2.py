def reorder(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] in d[arr[-1-i]]:
                arr.insert(len(arr)-i, arr[j])
                del arr[j]
                return reorder(arr)
    return arr

d = dict()

with open("day5_1.txt", "r") as f:
    rules = f.readlines()
    
with open("day5_2.txt", "r") as f:
    data = f.readlines()
data = [[int(i) for i in d.split(",")] for d in data]

for rule in rules:
    s = [int(i) for i in rule.split("|")]
    
    if not s[0] in d:
        d[s[0]] = [s[1]]
    else:
        d[s[0]].append(s[1])

result = 0
for line in data:
    ordered = reorder(line.copy())
    if ordered != line:
        result += ordered[int(len(line)/2)]

print(result)