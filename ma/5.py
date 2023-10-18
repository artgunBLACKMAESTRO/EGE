with open('5') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=list(map(int,a))
a.sort()
ot=[]
b=[a[0]]
a.pop(0)
i=0
while a:
    if a[i]-b[-1]>=7:
        b.append(a[i])
        a.pop(i)
    else:
        i+=1
    if len(a)<=i:
        i=0
        ot.append(b)
        print(a)
        b=[a[0]]
        a.pop(0)
print(len(ot),ot,len(a))
