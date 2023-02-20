with open('27-3201') as f:
    s = f.read().strip().split('\n')

s.pop(0)
s = [(int(i.split()[0]), int(i.split()[1])) for i in s]
maxResult = 0
minResult = 0
D = 7

m = [10**10] * D
for i in s:
    maxResult += max(i)
    minResult += min(i)
    d = max(i) - min(i)
    r = d % D
    if r > 0:
        newM = m.copy()
        for k in range(1, D):
            r0 = (r + k) % D
            newM[r0] = min(newM[r0], d + m[k])
        newM[r] = min(newM[r], d)
        m = newM

if maxResult % D == minResult % D:
    print(maxResult)
else:
    print(maxResult - m[(maxResult % D) - minResult % D])