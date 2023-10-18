f=open('27-15A')
a=f.read()
a=a.split('\n')
a=[list(map(int,a[i].split(' '))) for i in range(len(a))]
k=[0]
D=109
for i in a:
    comb=[x+y for x in i for y in k]
    comb.sort()
    k={x%D : x for x in comb}
    k=k.values()
m=0
for i in k:
    if i%D!=0:
        m=max(m,i)
print(m)