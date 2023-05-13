with open('26-5232') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
a=sorted(a)
d=[[] for _ in range(10001)]
for i in range(len(a)):
    d[a[i][0]].append(a[i][1])
m=0
b=0
for i in range(len(d)):
    k=0
    for z in range(len(d[i])):
        if d[i][z]:
            if d[i][z]%2==1:
                k+=1
    if k>b:
        m=i
        b=k
print(b,m)