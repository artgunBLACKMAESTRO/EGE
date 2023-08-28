f=open('27-shaB')
a=f.read().strip()
a=a.split('\n')
a.pop(0)
k=int(a.pop(0))
r=int(a.pop(0))
a=list(map(int,a))
d=[]
for i in range(len(a)):
    d.append(a[i]%100)
count=0
for i in range(len(d)):
    l=d[i+1:i+k+1]
    count+=d[i+r:i+k+1].count((77-d[i]))+d[i+r:i+k+1].count((177-d[i]))
print(count)