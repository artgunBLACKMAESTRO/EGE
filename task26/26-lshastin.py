with open('26-lshastin') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
a=[list(map(int,i.split())) for i in a]
d=[[] for _ in range(max([x[0] for x in a])+1)]
for i in range(len(a)):
    d[a[i][0]].append(a[i][1])

for i in d:
    i.sort()
c=0
m=0
for i in range(1,len(d)):
    for z in range(1,len(d[i])-1):
        if d[i][z]-d[i][z-1]==6 and d[i][z+1]-d[i][z]==6:
            m=i
            c+=1
print(m,c)