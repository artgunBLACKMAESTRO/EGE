with open('26-28') as f:
    a=f.read()
a=a.split('\n')
a=[[int(a[i].split()[0]),a[i].split()[1]] for i in range(len(a))]
a=sorted(a,key=lambda x: -x[0])
b=[a[3]]
print(a)
a.pop(3)
ot=[]
while a:
    i=0
    while i!=(len(a)-1):
        if (b[-1][0]-a[i][0])>=5 and (a[i][1]!=b[-1][0]):
            b.append(a[i])
            a.pop(i)
        else:
            i+=1
    ot.append(b)
    b=[a[0]]
    a.pop(0)
print(a)
print(max([len(x) for x in ot]))
print(len(ot),b)