with open('26-8482') as f:
    a = f.read()
a = a.split('\n')
a.pop(0)
k = int(a.pop(0))
a = [list(map(int, a[i].split())) for i in range(len(a))]
a.sort()
d = []
for i in range(k):
    d.append(0)
otv1 = 0
otv2 = 0
for i in range(len(a)):
    for z in range(len(d)):
        flag = True
        if (a[i][0] - d[z]) >= 6:
            d[z] = a[i][1]
            flag = False
            otv1 += 1
            otv2 = z + 1
            break
    if flag:
        w = 0
        for q in range(len(d)):
            if w < d[q]:
                w = d[q]
                ind = q
        if (d[q] - (a[i][0] + 10)) >= 6:
            d[q] = a[i][1] + 10
            otv1 += 1
            otv2 = q + 1
print(otv1, otv2)
