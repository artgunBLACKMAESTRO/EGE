import math
with open('27-6041A') as f:
    a = f.read()
a = a.split('\n')
a.pop(0)
a = list(map(int, a))
c = 0
m = ''
for i in range(len(a)//2):
    c = 0
    k = (i + len(a) // 2) % len(a)
    for z in range(math.ceil(len(a) / 4)):
        c += z * a[(i + z) % len(a)] + z * a[i - z]
        c += z * a[k - z] + z * a[(k + z) % len(a)]
    if m == '':
        m = c
    elif m > c:
        m = c
print(m)


