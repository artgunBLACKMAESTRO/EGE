from math import ceil as okryg
with open('27-6638A') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
sum=99999999999
for i in range(len(a)):
    x=0
    for z in range(len(a)):
        if a[i][0]!=a[z][0]:
            x+=abs(a[i][0]-a[z][0])*okryg(a[z][1]/100)
    if sum>x:
        sum=x
        l=a[i][0]
print(l)