with open('27-8281B') as f:
    a=f.read()
a=a.split('\n')
a.pop(0)
k=int(a.pop(0))
a=list(map(int,a))
d=[]
for i in range(len(a)):
    d.append(a[i]%8)
count=0
for i in range(len(d)):
    l=d[i+1:i+k+1]
    count+=d[i+1:i+k+1].count((8-d[i])%8)
print(count)