import time
d = {}
with open("AFINN-111.txt", encoding='utf-8') as f:
    for line in f:
        (key, val) = line.split('\t')
        d[key] = val
print(d)

