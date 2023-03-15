with open('27-5134B') as f:
    a = f.read()
a = a.split('\n')
a.pop(0)
a = list(map(int, a))
D = 524288
c = 0
for i in range(len(a)):
    x = i
    k = 1
    while x != (len(a)) and ((a[x] * k) % D) != 0:
        k = a[x] * k
        c += 1
        x += 1
print(c)
