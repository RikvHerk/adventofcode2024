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
    brk = False
    for i in range(len(line)-1):
        for j in range(len(line)-i-1):
            if line[j] in d[line[-1-i]]:
                brk = True
                break
        if brk:
            break
    if not brk:
        result += line[int(len(line)/2)] 
    

print(result)