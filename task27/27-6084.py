with open('27A-6084') as f:
    a=f.read()
a=a.split('\n')
a=[list(map(int,i.split())) for i in a]
k=a[0][1]
a.pop(0)
a.sort()
d=[[a[i][0],a[i][1]%2] for i in range(len(a))]
print(d)

