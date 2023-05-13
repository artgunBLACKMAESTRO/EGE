import math

with open('27-6760') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
m=99999999
for i in range(len(a)):
    c=0
    for z in range(len(a)):
        c+=abs(a[i][0]-a[z][0])*(math.ceil(a[z][1]/48))
    m=min(m,c)
print(m)