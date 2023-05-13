with open('26-6094') as f:
    a=f.read()
a=a.split('\n')
k=list(map(int,a[0].split(' ')))[1]
m=list(map(int,a[0].split(' ')))[2]
a.pop(0)
a=[[int(x.split(' ')[0]),x.split(' ')[1]] for x in a]
a=sorted(a, key=lambda x: x[0])
ot=[]
i=0
while i!=len(a):
    s=[a[i]]
    l=i+1
    i+=1
    while l!=len(a) and len(s)!=m:
        if (a[l][0]-s[-1][0])>=k and s[-1][1]!=a[l][1]:
            s.append(a[l])
            a.pop(l)
        else:
            l+=1
    ot.append(s)
m=0
for i in ot:
    m=max(m,len(i))
c=0
for i in ot:
    if len(i)==m:
        c+=1
print(len(ot),c)