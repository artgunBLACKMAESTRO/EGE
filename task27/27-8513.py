with open('27-8513B') as f:
    a=f.read().strip()
a=list(map(int,a.split('\n')))
k=a.pop(0)
a.pop(0)
m=0
z=0
for i in range(k,len(a)):
    z=max(z,a[i-k])
    m=max(m,z+a[i])
print(m)