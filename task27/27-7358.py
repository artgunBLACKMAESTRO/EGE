
from math import gcd as nod
with open('27-7358') as f:
    a=f.read()
a=list(map(int,a.split('\n')))
a.pop(0)
m=0
g=0
for i in range(len(a)-1):
    b=[]
    for z in range(i,len(a)):
        b.append(a[z])
        h=gcd
        if h>=g:
            g=h
            m=max(m,sum(b))

print(m)
