with open('27-5324A') as f:
    a=f.read()
a=a.split('\n')
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
m=999999999999
vm=5
for i in range(len(a)):
    k=a[0]
    c=0
    for z in range(len(a)):
        if a[z][1]%5!=0:
            j=a[z][1]//5+1
        else:
            j=a[z][1]/5
        c+=abs(a[z][0]-a[i][0])*j
    m=min(m,c)
print(m)