with open('9-6602') as f:
    a = f.read().split('\n')
a = [list(map(int, a[i].split('\t'))) for i in range(len(a))]
k = 0
for i in range(len(a)):
    l = 0
    pov = 0
    nepov = 0
    for z in a[i]:
        for k in a[i]:
            if z == k:
                l += 1
    if l == 8:
        for z in a[i]:
            p = 0
            for k in a[i]:
                if z == k:
                    p += 1
            if p == 2:
                pov += z
            else:
                nepov += z
        if (nepov / 4) >= pov:
            k += 1
print(k)
