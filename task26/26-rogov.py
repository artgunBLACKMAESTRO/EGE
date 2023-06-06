with open('26-rogovtest') as f:
    a = f.read()
a = a.split('\n')
k = int(a.pop(0))
a.pop(0)
a = [[int(a[i].split()[0]), int(a[i].split()[1])] for i in range(len(a))]
d = [0] * k
c = 0
vr = 0
a = sorted(a, key=lambda x: x[0])
print(a)
for i in range(len(a)):
    for z in range(len(d)):
        flag = True
        if d[z] < a[i][0]:
            d[z] = a[i][1] + a[i][0]
            if d.count()
            if z == (k - 1):
                vr += abs(a[i][0] - min(d))
            flag = False
            break
    if flag:
        c += 1
print(c, vr)
