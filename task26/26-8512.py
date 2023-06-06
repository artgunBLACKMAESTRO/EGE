with open('26-8512') as f:
    a=f.read()
a=a.split('\n')
k=int(a.pop(0))
a.pop(0)
a=[list(map(int,a[i].split())) for i in range(len(a))]
a.sort()
c=0
l=0
d=[0 for _ in range(k)]
for i in range(len(a)):
    for z in range(k):
        if d[z]<a[i][0]:
            d[z]=a[i][1]
            c+=1
            l=z+1
            break
print(c,l)